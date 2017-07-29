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
    "git": {},
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
