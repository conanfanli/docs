Rice or die
===========
# Weapons
## Vim
` make play -- --tags vim`

## Bash
- ~/.bashrc loads ~/.rice.bash
- Run `checkifriceiscooked` to diff bash configuration
- Run `cooksomerice` to sync bash configuration
- Press `ALT-C` to go to a directory
- `cmds` to choose one of the alasies or functions defined in ~/.rice.bash

# HOW TO

## Stream subprocess stdin and stdout
https://kevinmccarthy.org/2016/07/25/streaming-subprocess-stdin-and-stdout-with-asyncio-in-python/

## Pass arguments to make commands
```
test: ## Run tests for the application
	run-my-command $(filter-out $@,$(MAKECMDGOALS))
```

# Docker

## Clean up images and volumes
`alias dockerclean='(docker ps -aq | xargs docker rm); (docker images -aq -f dangling=true | xargs docker rmi); docker volume rm $(docker volume ls -qf dangling=true)'`

## User Namespaces
[How to User Namespaces in Docker Engine](https://success.docker.com/KBase/Introduction_to_User_Namespaces_in_Docker_Engine)

# Regex
- Use look ahead and lookbehind to print out the only the matching group. For example `ag '(?<=alias )(.*?)(?=\=)` will print out the string between `alias` and `=`.

# Postgres
## Insert rows from CSV file
`\copy companies from 'companies.csv' with csv;`

# Django
- Make sure `multi_db = True` in test cases when working with multiple databases. Otherwise, DB won't be flushed after every test.

