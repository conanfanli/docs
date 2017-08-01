Setting up a development environment
====================================
# Weapons
## Vim

### Install on Mac
- Make sure xcode is updated by checking AppStore
- `brew install vim --override-system-vim --with-python3`

### Install on Linux
- Run [compile-vim.sh](compile-vim.sh) by doing `./compile-vim.sh python3` (change to python2 to compile with python 2)
- Alternatively, run `curl -sSL https://raw.githubusercontent.com/conanfanli/docs/master/compile-vim.sh | bash -s python3`

## fzf
Install by running `./packages.sh`

## ag
Install by running `./packages.sh`

# State design
```javascript
{
  "system": "osx",
  "weapons": {
    "vim": {
      "installed": true,
      "version": "8.0"
    },
    "fzf": {
      "installed": true
    },
    "ag": {
      "installed": true
    },
    "tmux": {
      "installed": true,
      "version": "2.5",
      "configurations": {
        "configurations/tmux/tmux.conf": {
          "inSync": true,
          "destination": "~/.tmux.conf"
        },
        "configurations/tmux/tmux.conf.local": {
          "inSync": false,
          "destination": "~/.tmux.conf.local",
          "diff": "xxxx"
        }
      }
    }
  }
}
```

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
