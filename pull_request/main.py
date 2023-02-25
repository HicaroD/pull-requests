import asyncio

from pull_request.command_line_argument_parser import CommandLineArgumentParser
from pull_request.credential_manager import CredentialManager
from pull_request.exceptions import CredentialFileDoesNotExist, InvalidFormatForCredentialFile
from pull_request.pullrequest import PullRequest, PullRequestData


async def main():
    try:
        argument_parser = CommandLineArgumentParser()
        args = argument_parser.parse_args()

        pr_content = PullRequestData(
            args["title"], args["body"], args["from"], args["to"]
        )

        credential_manager = CredentialManager()
        credentials = credential_manager.read_credential_file()

        pr = PullRequest(credentials, pr_content)
        await pr.make_pull_request()

    except InvalidFormatForCredentialFile:
        print(
            "Error: Make sure your 'pr.json' has all required files: 'username', 'repository' and 'token'."
        )
    except CredentialFileDoesNotExist:
        print("Error: Make sure your 'pr.json' file exists in the root directory of your project.")
        


def _main():
    asyncio.run(main())


if __name__ == "__main__":
    _main()
