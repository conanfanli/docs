Setting up a development environment
====================================
# Weapons
## Vim
` make play -- --tags vim`

## Bash
- ~/.bashrc loads ~/.rice.bash
- Run `checkifriceiscooked` to diff bash configuration
- Run `cooksomerice` to sync bash configuration

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
