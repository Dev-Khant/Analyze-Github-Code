from LLM.scrap import scrap_repo


class AnalyzeRepo:
    def __init__(self, token, url):
        self.token = token

        parsed_url = url.split("/")
        self.github_owner = parsed_url[-2]  # Get the owner
        self.github_repo_name = parsed_url[-1]  # Get the repo name
        self.github_access_token = ""

    def run(self):
        result = scrap_repo(
            self.github_owner, self.github_repo_name, self.github_access_token
        )
