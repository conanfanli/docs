[![Build Status](https://travis-ci.org/conanfanli/rice.svg?branch=master)](https://travis-ci.org/conanfanli/rice)

# Table of contents
- [Rice or die](#rice-or-die)
- [Provisioning](#provisioning)
  * [Setup a new box](#setup-a-new-box)
  * [Only run tasks with tags](#only-run-tasks-with-tags)
- [Bash, Shell, Commands](#bash-shell-commands)
  * [General](#general)
  * [Regex](#regex)
- [Python](#python)
- [Django](#django)
  * [Write decorators with arguments](#write-decorators-with-arguments)
  * [Stream subprocess stdin and stdout](#stream-subprocess-stdin-and-stdout)
- [Makefile](#makefile)
  * [Pass arguments to make commands](#pass-arguments-to-make-commands)
  * [Assign result of a command to a variable in Makefile](#assign-result-of-a-command-to-a-variable-in-makefile)
- [Docker](#docker)
  * [Edit local python packages and sync to docker container](#edit-local-python-packages-and-sync-to-docker-container)
  * [Clean up images and volumes](#clean-up-images-and-volumes)
- [Postgres](#postgres)
  * [Insert rows from CSV file](#insert-rows-from-csv-file)
- [Heroku](#heroku)
- [Github](#github)

# Provisioning. See [here](ansible/README.md)

# Bash, Shell, Commands

## General
- ~/.bashrc loads ~/.rice.bash
- Press `ALT-C` to go to a directory
- `cmds` to choose one of the alasies or functions defined in [rice.shell.template.sh](ansible/roles/common/files/rice-shell.template.sh)
- Find all tsx files: `ag -g tsx`
- Highlight text using `grep`: `command_here | grep --color -E '^|pattern1|pattern2'`

## Regex
- Use look ahead and lookbehind to print out the only the matching group. For example `ag '(?<=alias )(.*?)(?=\=)` will print out the string between `alias` and `=`.

# Python
## Create mypy compatible decorator
```
FuncType = TypeVar('FuncType', bound=Callable[..., Any])
def fart_without_making_a_sound(loudness: int) -> Callable[[FuncType], FuncType]:
    def decorator(func: FuncType) -> FuncType:
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            # Cover your bum with your hand
            # Fart
            # Smell your hand
            pass
        return cast(FuncType, func_wrapper)
    return decorator
```

# Django
- Make sure `multi_db = True` in test cases when working with multiple databases. Otherwise, DB won't be flushed after every test.

## Write decorators with arguments
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#decorators-with-arguments

## Stream subprocess stdin and stdout
https://kevinmccarthy.org/2016/07/25/streaming-subprocess-stdin-and-stdout-with-asyncio-in-python/

# Makefile
Good examples:
- https://github.com/thockin/go-build-template/blob/master/Makefile
## Pass arguments to make commands
```
test: ## Run tests for the application
	run-my-command $(filter-out $@,$(MAKECMDGOALS))
```

## Assign result of a command to a variable in Makefile
`myvar=$(shell somecommand)`

# Docker

## Optimizing Dockerfile caching for pip
https://www.aptible.com/documentation/enclave/tutorials/faq/dockerfile-caching/pip-dockerfile-caching.html
https://lekum.org/post/multistage-dockerfile/

## Edit local python packages and sync to docker container
We sometimes need to edit installed Python packages. This is not too straightforward with docker containers. If the package is install on the host in a virtual environment. Use this [script](copy-package-to-container.sh) to copy from the host to the container.

Usage: `copy-package-to-container.sh container_name package_name`

## Clean up images and volumes
`alias dockerclean='(docker ps -aq | xargs docker rm); (docker images -aq -f dangling=true | xargs docker rmi); docker volume rm $(docker volume ls -qf dangling=true)'`
Newer versions of docker now supports `docker system prune`

# Tmux
- `ctrl-a alt-2` to switch layout

# Postgres
## Insert rows from CSV file
`\copy companies from 'companies.csv' with csv;`

# Heroku

- Create App with name `heroku apps:create myapp`
- Stop web: `heroku ps:scale web=0`
- Add addon `heroku addons:create heroku-redis --app important-app` or `heroku addons:create heroku-postgresql`. This might create duplicate addons

# Github
- You can deploy to a branch `gh-pages` and the content will be pushed github pages at `https://username.github.io/project_name`

# Google Cloud Platform
https://cloud.google.com/sdk/docs/
