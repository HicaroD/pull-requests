#! /usr/bin/env node

const { postPullRequest } = require("./github.js");

const main = async () => {
    postPullRequest({
	title: "PR TITLE",
	base_branch: "master",
	configuration: {
	    "username": "GITHUB_USERNAME",
	    "repository": "REPOSITORY_NAME",
	    "token": "Bearer TOKEN_HERE",
	}
    });
}

main()
