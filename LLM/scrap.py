import logging
from github import Auth, Github
from LLM.generate import LLM_Summarize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ScrapRepo")

exclude_extensions = [
    "png",
    "jpg",
    "jpeg",
    "svg",
]  # exclude files with these extensions
no_decode_extensions = ["md", "html"]  # No ASCII decoding


def scrap_repo(github_owner, github_repo_name, github_access_token, llm_token):
    """
    Function to traverse through each file in Repo
    Pass each code file to LLM and get summary
    """

    # Setup Github and OpenAI
    auth = Auth.Token(github_access_token)
    g = Github(auth=auth)
    get_summary = LLM_Summarize(llm_token)

    logger.info("Github & OpenAI set")

    # Get repo contents
    repo = g.get_repo(f"{github_owner}/{github_repo_name}")
    contents = repo.get_contents("")
    summary_list = []

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":  # if dir traverse recursively
            contents.extend(repo.get_contents(file_content.path))
        else:
            extension = file_content.path.split(".")[-1]  # Get file extension
            if extension in exclude_extensions:
                continue
            elif extension in no_decode_extensions:
                text = (
                    file_content.decoded_content.decode()
                )  # No ASCII decoding, get raw content
            else:
                text = file_content.decoded_content.decode("ASCII")

            # Get summary of each code file
            code_summary = get_summary.summarize_code(text)
            logger.info(f"Code Summary {code_summary}")
            summary_list.append(code_summary)
            break

    logger.info("Summarizing all code")
    summary = get_summary.summarize_repo(llm_token, summary_list)
    return summary
