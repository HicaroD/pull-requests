#! /usr/bin/env node

const fs = require("fs");
const { postPullRequest } = require("./github.js");

const main = async () => {
    fs.readFile("pr.json", (error, data) => {
	if(error) {
	    console.log("Unable to open pr.json. Make sure it is located on the root directory"); 
	    process.exit(1);
	}	

	let config_file = JSON.parse(data.toString())

	postPullRequest({
	    title: "PR TITLE",
	    base_branch: "master",
	    configuration: config_file,
	});
    });
}

main()
