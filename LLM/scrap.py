from github import Auth, Github
from LLM.llm import summarize_code, summarize_repo


def scrap_repo(github_owner, github_repo_name, github_access_token, llm_token):
    auth = Auth.Token(github_access_token)
    g = Github(auth=auth)

    repo = g.get_repo(f"{github_owner}/{github_repo_name}")
    contents = repo.get_contents("")
    summary_list = []

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            code_summary = summarize_code(llm_token, file_content)
            summary_list.append(code_summary)

    summary = summarize_repo(llm_token, summary_list)
    return summary
