from github import Auth, Github
from LLM.llm import summarize


def scrap_repo(github_owner, github_repo_name, github_access_token):
    auth = Auth.Token(github_access_token)
    g = Github(auth=auth)

    repo = g.get_repo(f"{github_owner}/{github_repo_name}")
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            # summarize
            contents.extend(repo.get_contents(file_content.path))
        else:
            print(file_content)

    file_content = repo.get_contents("setup.py")
    text = file_content.decoded_content.decode("ASCII")
    print(file_content.path)
