from dataclasses import dataclass
import requests
import json


@dataclass
class Credentials:
    username: str
    repository_name: str
    token: str

    def get_token(self) -> str:
        return "Bearer " + self.token


@dataclass
class PullRequestData:
    head_branch: str
    base_branch: str
    title: str
    body: str | None


class PullRequest:
    def __init__(self, credentials: Credentials, pr_content: PullRequestData) -> None:
        self.credentials = credentials
        self.pr_content = pr_content

    async def make_pr(self):
        token = self.credentials.get_token()

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": token,
            "Content-Type": "application/json",
        }
        print(headers)
        body = {
            "title": self.pr_content.title,
            "base": self.pr_content.base_branch,
            "head": f"{self.credentials.username}:{self.pr_content.head_branch}",
            "body": self.pr_content.body if self.pr_content.body is not None else "",
        }
        print(body)
        url = f"https://api.github.com/repos/{self.credentials.username}/{self.credentials.repository_name}/pulls"

        response = requests.post(url, headers=headers, json=body)
        match response.status_code:
            case 201:
                print(
                    f"Pull request from '{self.pr_content.head_branch}' to '{self.pr_content.base_branch}' was successfully made"
                )
            case 403:
                print(
                    "You're probably spamming it. Try again later or check if there are changes to make a pull request"
                )
            case _:
                print("Unexpected behavior")
                print(
                    f"STATUS CODE: {response.status_code}\nRESPONSE BODY: {response.json()}"
                )
        exit(1)
