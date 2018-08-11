[![Build Status](https://travis-ci.org/conanfanli/rice.svg?branch=master)](https://travis-ci.org/conanfanli/rice)

# Provisioning. See [here](ansible/README.md)

# Productivity: Bash, Shell, Commands
## Shorcuts
- `ctrl-a alt-2` to switch layout in `tmux`
- `ctrl-e` to jump to end of line. `ctrl-a` won't work as jump to start because it's mapped in `tmux`. Use `alt-b` to go back one word at a time.


## Vim
- use `silent! py3 pass` in vimrc to supress python3.7 warnings
- Install YouCompleteMe with `./install.py --gocode-completer --tern-completer --clang-completer` in Python2

## General shell stuff
- ~/.bashrc loads ~/.rice.bash which is generated from [rice-shell.template.sh](ansible/roles/common/files/rice-shell.template.sh)
- Press `ALT-C` to go to a directory
- `cmds` to choose one of the alasies or functions defined in [rice.shell.template.sh](ansible/roles/common/files/rice-shell.template.sh)
- Find all tsx files: `ag -g tsx`
- Highlight text using `grep`: `command_here | grep --color -E '^|pattern1|pattern2'`

## Regex
- Use look ahead and lookbehind to print out the only the matching group. For example `ag '(?<=alias )(.*?)(?=\=)` will print out the string between `alias` and `=`.

# Python
## Install Python3.7 on ubuntu
Follow https://blog.softhints.com/ubuntu-how-to-install-latest-python-and-list-all-python-versions/
and then run `sudo apt install python3.7-venv python3.7-dev`

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

# Sumo example
```
_source=prod AND _sourceHost=appName* AND NOT _sourceName=nginx AND NOT "shit I do not want" | json auto nodrop | where !(name matches "crap.*") | last(asctime) as start_time ,first(asctime) as finish_time, first(_messageTime) as finish_time_epoch, last(_messageTime) as start_time_epoch group by some_id | finish_time_epoch - start_time_epoch as time_diff 
```
