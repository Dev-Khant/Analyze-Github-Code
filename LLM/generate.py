import logging

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GenerateSummary")


class LLM_Summarize:
    """Perform all LLM operations"""

    def __init__(self, llm_token):
        self.llm = ChatOpenAI(temperature=0.1, openai_api_key=llm_token)
        self.code_summmary_prompt = (
            "Summarize code in 50-70 words in paragraph : {code}"
        )
        self.code_init_prompt = "You are an elite programmer who can understand Github Repository code give to you in text very well and summarize what is written in it."

    def summarize_code(self, text):
        """
        Get summary for each code file
        Use Langchain Memory to set init_prompt
        """

        # Prepare prompt for code
        prompt_temp = ChatPromptTemplate.from_template(self.code_summmary_prompt)
        prompt = prompt_temp.format_messages(code=text)

        # Set memory with default prompt
        memory = ConversationBufferMemory()
        memory.save_context(
            {"input": self.code_init_prompt},
            {
                "output": "Of course! I'd be happy to help you understand the code from the Github repository you provide. Please share the code with me, and I'll do my best to summarize its contents for you."
            },
        )

        logger.info("Prompt & Memeory set for code summary")

        # Create conversation using memory
        # Get code summary from conversation
        conversation = ConversationChain(llm=self.llm, memory=memory, verbose=False)
        code_summarized = conversation.predict(input=prompt)

        logger.info("Code summary generated")

        return code_summarized

    def summarize_repo(llm_token, summarize_list):
        """
        Combine all different summaries from code files
        Generate a detailed summary of repo
        """
        pass
