import logging

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GenerateSummary")


class LLM_Summarize:
    """Perform all LLM operations"""

    def __init__(self, llm_token):
        self.llm = ChatOpenAI(temperature=0.1, openai_api_key=llm_token)
        self.code_summmary_prompt = """You are an elite programmer who can understand Github Repository code give to you in text very
                                     well and summarize what is written in it.

                                    Code : {text}

                                    Summarize the above code present between delimiters in 50-70 words and in paragraph"""
        self.all_summary_prompt = """You are great at understanding bigger picture of a codebase by looking at summary of different code 
                                    files. Given the following summaries and you have to tell in detail what does the project do.
                                     
                                    Summaries : {summary_list}

                                    Limit final summary to 2000 words. Provide an elegant answer highlighting its purpose, 
                                    main features, and key technologies used. Include 2-3 emojis. Response will be shown in HTML page
                                    inside a <p> tag so make it compatible with it.
                                    
                                    """

    def summarize_repo(self, code_list):
        """
        Combine all different summaries from code files
        Generate a detailed summary of repo
        """

        code_list = [Document(page_content=code) for code in code_list]

        # Prompt to use in map and reduce stages
        CODE_SUMMARY = PromptTemplate(
            template=self.code_summmary_prompt, input_variables=["text"]
        )
        ALL_SUMMARY = PromptTemplate(
            template=self.all_summary_prompt, input_variables=["summary_list"]
        )

        logger.info("Prompt Ready")

        chain = load_summarize_chain(
            self.llm,
            chain_type="map_reduce",
            map_prompt=CODE_SUMMARY,
            combine_prompt=ALL_SUMMARY,
            combine_document_variable_name="summary_list",
        )
        logger.info("Running LLM")

        result = chain({"input_documents": code_list}, return_only_outputs=True)
        logger.info("Result Generated")

        return result
