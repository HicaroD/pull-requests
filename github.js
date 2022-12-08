const axios = require("axios");

const reportError = (response) => {
    if(!response) {
	console.log("Unexpected error!");
    }

    let status_code = response.status;
    if(status_code === 422) {
	console.log("Make sure there are changes in order to make a PR.");
    } else {
	console.log("Forbidden! Have you passed the right credentials?");
    }
}

const postPullRequest = async ({title, base_branch, head_branch, configuration}) => {
    if (title === undefined || base_branch === undefined) {
	console.log("Title and/or base branch should not be empty");
    }

    let body = {
	"title": title,
	"base": base_branch,
	"head": `${configuration.username}:${head_branch}`
    };
    let headers = {
	"Accept": "application/vnd.github+json", 
	"Authorization": `Bearer ${configuration.token}`,
	"Content-Type": "application/json",
    };
    let endpoint_url = `https://api.github.com/repos/${configuration.username}/${configuration.repository}/pulls`;

    await axios
	.post(
	    endpoint_url,
	    body,
	    { headers: headers }
        )
	.then(() => {
	    console.log(`Pull request from "${head_branch}" was successfuly created on "${base_branch}"`)
	}, (error) => {
	    reportError(error.response);
	}
    );
}

module.exports = { postPullRequest };
