#! /usr/bin/env node

const fs = require("fs")
const yargs = require("yargs")
const {hideBin} = require("yargs/helpers");
const { postPullRequest } = require("./github.js")
const argv = yargs(hideBin(process.argv)).argv

const main = async () => {
    if(typeof argv.from === undefined) {
	console.log("You should pass a valid head branch name using the --from flag");
	process.exit(1);
    }
    if(typeof argv.to === undefined) {
	console.log("You should pass a valid base branch name using the --to flag");
	process.exit(1);
    }
    let head_branch = argv.from;
    let base_branch = argv.to;

    fs.readFile("pr.json", (error, data) => {
	if(error) {
	    console.log("Unable to open pr.json. Make sure it is located on the project root directory"); 
	    process.exit(1);
	}	

	let config_file = JSON.parse(data.toString())

	postPullRequest({
	    title: "PR TITLE",
	    base_branch: base_branch,
	    head_branch: head_branch,
	    configuration: config_file,
	});
    });
}

main()
