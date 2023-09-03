import logging

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import LLMChain, ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GenerateSummary")


class LLM_Summarize:
    """Perform all LLM operations"""

    def __init__(self, llm_token):
        self.llm = ChatOpenAI(temperature=0.1, openai_api_key=llm_token)
        self.code_summary_prompt = """You are an elite programmer who can understand Github Repository code give to you in text very
                                     well and summarize what is written in it.

                                    Code : {codes}

                                    Summarize the above list of codes present between delimiters in 50-70 words each and in paragraph.
                                    Store it in a list."""
        self.all_summary_prompt = """You are great at understanding bigger picture of a codebase by looking at summary of different code 
                                    files. Given the following summaries and you have to tell in detail what does the project do.
                                     
                                    Summaries : {summary_list}

                                    Limit final summary to 2000 words. Provide an elegant answer highlighting its purpose, 
                                    main features, and key technologies used. Include 2-3 emojis."""
        self.format_response = """
                                Given a below text modify it in HTML format for <p> tag. Use proper spacing, replace all space and line break with required
                                HTML tags. Highlight main words by using proper tags. Include headings if required.

                                Text : {text} 
                                """

    def summarize_repo(self, code_list):
        """
        Combine all different summaries from code files
        Generate a detailed summary of repo
        """

        code_list = [Document(page_content=code) for code in code_list]

        # Map
        MAP_PROMPT = PromptTemplate.from_template(template=self.code_summary_prompt)
        map_chain = LLMChain(llm=self.llm, prompt=MAP_PROMPT)

        # Reduce
        REDUCE_PROMPT = PromptTemplate.from_template(template=self.all_summary_prompt)
        reduce_chain = LLMChain(llm=self.llm, prompt=REDUCE_PROMPT)

        logger.info("Prompt Ready")

        combine_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain, document_variable_name="summary_list"
        )
        reduce_documents_chain = ReduceDocumentsChain(
            combine_documents_chain=combine_documents_chain,
            collapse_documents_chain=combine_documents_chain,
            token_max=4000,
        )

        map_reduce_chain = MapReduceDocumentsChain(
            llm_chain=map_chain,
            reduce_documents_chain=reduce_documents_chain,
            document_variable_name="codes",
            return_intermediate_steps=False,
        )

        # Split text
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000, chunk_overlap=0
        )
        split_docs = text_splitter.split_documents(code_list)

        logger.info("Running LLM")
        result = map_reduce_chain.run(split_docs)

        # Change response from LLM to HTML format
        FORMAT_PROMPT = ChatPromptTemplate.from_template(self.format_response)
        FORMAT_MSG = FORMAT_PROMPT.format_messages(text=result)
        response = self.llm(FORMAT_MSG).content

        logger.info("Result Generated")

        return response
