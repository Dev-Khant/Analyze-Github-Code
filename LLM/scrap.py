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
    "pkl",
    "gitignore",
    "txt",
]  # exclude files with these extensions


def scrap_repo(github_owner, github_repo_name, llm_token):
    """
    Function to traverse through each file in Repo
    Pass each code file to LLM and get summary
    """

    # Setup Github and OpenAI
    g = Github()
    get_summary = LLM_Summarize(llm_token)

    logger.info("Github & OpenAI set")

    # Get repo contents
    repo = g.get_repo(f"{github_owner}/{github_repo_name}")
    contents = repo.get_contents("")
    code_list = []

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":  # if dir traverse recursively
            contents.extend(repo.get_contents(file_content.path))
        else:
            extension = file_content.path.split(".")[-1]  # Get file extension
            if extension in exclude_extensions:
                continue
            text = file_content.decoded_content.decode()

            code_list.append(text)

    logger.info("Summarizing all code")
    summary = get_summary.summarize_repo(code_list)
    return summary
