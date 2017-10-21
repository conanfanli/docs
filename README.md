Rice or die
===========
[![Build Status](https://travis-ci.org/conanfanli/rice.svg?branch=master)](https://travis-ci.org/conanfanli/rice)

# Provisioning

## Setup a new box
- clone this repo
- Install ansible: `sudo apt-get update && sudo apt install python3-pip && sudo pip3 install ansible`
- `make play`

## Only run tasks with tags
- Only setup vim:` make play -- --tags vim` or `make paly-tags vim`

# Bash, Shell, Commands

## General
- ~/.bashrc loads ~/.rice.bash
- Press `ALT-C` to go to a directory
- `cmds` to choose one of the alasies or functions defined in [rice.shell.template.sh](ansible/roles/common/files/rice-shell.template.sh)

## Regex
- Use look ahead and lookbehind to print out the only the matching group. For example `ag '(?<=alias )(.*?)(?=\=)` will print out the string between `alias` and `=`.

# Python

# Django
- Make sure `multi_db = True` in test cases when working with multiple databases. Otherwise, DB won't be flushed after every test.

## Write decorators with arguments
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#decorators-with-arguments

## Stream subprocess stdin and stdout
https://kevinmccarthy.org/2016/07/25/streaming-subprocess-stdin-and-stdout-with-asyncio-in-python/

# Makefile
## Pass arguments to make commands
```
test: ## Run tests for the application
	run-my-command $(filter-out $@,$(MAKECMDGOALS))
```

## Assign result of a command to a variable in Makefile
`myvar=$(shell somecommand)`

# Docker

## Edit local python packages and sync to docker container
We sometimes need to edit installed Python packages. This is not too straightforward with docker containers. If the package is install on the host in a virtual environment. Use this [script](copy-package-to-container.sh) to copy from the host to the container.

Usage: `copy-package-to-container.sh container_name package_name`

## Clean up images and volumes
`alias dockerclean='(docker ps -aq | xargs docker rm); (docker images -aq -f dangling=true | xargs docker rmi); docker volume rm $(docker volume ls -qf dangling=true)'`


# Postgres
## Insert rows from CSV file
`\copy companies from 'companies.csv' with csv;`

# Heroku

- Create App with name `heroku apps:create myapp`
- Stop web: `heroku ps:scale web=0`
- Add addon `heroku addons:create heroku-redis --app important-app` or `heroku addons:create heroku-postgresql`
