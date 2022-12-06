const axios = require("axios");

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

    let response = await axios
	.post(
	    endpoint_url,
	    body,
	    { headers: headers }
        )
	.then(({data}) => {
	   console.log(data)
	}
    );
}

module.exports = { postPullRequest };
