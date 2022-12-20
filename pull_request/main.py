import argparse
import json
import asyncio
from pull_request.pullrequest import PullRequest, Credentials, PullRequestData


def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pull requests on command line - Author: Icarus"
    )
    parser.add_argument(
        "-f", "--from", help="Changes are coming from this branch", required=True
    )
    parser.add_argument(
        "-t", "--to", help="Changes are going to that branch", required=True
    )
    parser.add_argument("-T", "--title", help="Pull request title", required=True)
    parser.add_argument("-b", "--body", help="Body of the pull request")
    return parser


def read_credentials() -> Credentials:
    with open("pr.json") as file:
        content = file.read()
        parsed_content = json.loads(content)
        # TODO: add error handling in case of KeyError
        return Credentials(
            parsed_content["username"],
            parsed_content["repository"],
            parsed_content["token"],
        )


async def main():
    argument_parser = get_argument_parser()
    args = vars(argument_parser.parse_args())

    pr_content = PullRequestData(args["from"], args["to"], args["title"], args["body"])
    credentials = read_credentials()
    pr = PullRequest(credentials, pr_content)
    await pr.make_pull_request()

def _main():
    asyncio.run(main())

if __name__ == "__main__":
    _main()
