export RICE_BASH_LOADED=1

if [ -f ~/bin/z.sh ]
then
    . ~/bin/z.sh
fi
alias tmux='tmux -2u'

export HISTFILESIZE=5000
# export LC_ALL=en_US.UTF-8
# export LANG=en_US.UTF-8
# export LANGUAGE=en_US.UTF-8
export EDITOR=vim

{% if ansible_os_family == 'Darwin' %}
# For MAC
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
# source bash_completion if the current shell is bash
(echo $SHELL | grep bash) && . $(brew --prefix)/etc/bash_completion
alias ls='ls -GFh'
{% else %}
alias ls='ls -GFh --color'
# END MAC
{% endif %}

IN_BASH=`echo $SHELL | grep bash`
# These only apply to bash
if [[ "$IN_BASH" ]]; then
    LS_COLORS="ow=01;96:di=01;96" ; export LS_COLORS
    PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
    alias so='source ~/.bashrc' #desc#: re-source ~/.bashrc
else
    alias so='source ~/.zshrc' #desc#: re-source ~/.zshrc
fi




# grep with color
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -FGlAhp'
alias la='ls -a'
alias ..='cd ../'
alias ...='cd ../../'

alias docs='cd ~/docs'
alias iconf='cd ~/projects/iconfigs'
alias t='python manage.py test'
alias sag='eval `ssh-agent` && ssh-add ~/.ssh/id_rsa'

hub () { # open the repo in github
    URL="https://github.com/$(git remote get-url origin | ag '(?<=:)(.*?)(?=\.git)' -o)"
    open $URL
}

fdir () { # Find directory matching pattern
    find . -type d -name $@ -print
}

alias checkifriceiscooked='cd ~/docs && make check -- --tags bash && cd -' # check if rice is updated
alias cooksomerice='cd ~/docs && make play -- --tags bash && source ~/.bashrc && cd -' # sync ~/.rice.bash
alias myip='curl https://ifconfig.co/'  # print my IP address

cmds () { # show all aliases and functions in a list
    selected=`~/docs/bin/get_all_aliases.py | fzf | ag -o '^(.*)(?=:)'`
    read -p "$selected " args

    eval "$selected $args"
}

v () { # activate virtualenv if there is one
    base=`basename $PWD`
    name=${1-$base}
    . ~/envs/$name/bin/activate 2> /dev/null || echo Available envs: `ls ~/envs`
}

ci () { # shortcut to git commit -a -m (if branch name contains ticket number, it will be included in the commit message
    ticket=`git branch | grep '*' | egrep '^[A-Z0-9]{2,5}-\d{1,4}' -o`
    [ -z "$1" ] && echo You forgot your fucking commit message! && return 1
    if [ -n "$ticket" ]; then
        git commit -a -m "$ticket: $*"
    else
        git commit -a -m "$*"
    fi
}

gdm () { # delete stale branches
    git branch --merged | grep -v '*' | xargs git branch -d
    git fetch -p
}

clip () {
    echo "$1" > /usr/share/nginx/html/clips/1.txt
}

change_extension () { # change file extentions in the current directory
    if [ -z "$1" ] || [ -z "$2" ]; then
        echo Missing 2 extensions
        return 1
    fi

    for file in *.$1; do
        mv "$file" "`basename "$file" .$1`.$2"
    done
}

alias dockerclean='(docker ps -aq | xargs docker rm); (docker images -aq -f dangling=true | xargs docker rmi); docker volume rm $(docker volume ls -qf dangling=true)'  # clean up docker containers and volumnes
alias dc='docker-compose'
export USER_ID=`id -u`
export PGUSER=postgres

export LESS_TERMCAP_mb=$'\e[01;31m'       # begin blinking
export LESS_TERMCAP_md=$'\e[01;38;5;74m'  # begin bold
export LESS_TERMCAP_me=$'\e[0m'           # end mode
export LESS_TERMCAP_se=$'\e[0m'           # end standout-mode
export LESS_TERMCAP_so=$'\e[38;5;246m'    # begin standout-mode - info box
export LESS_TERMCAP_ue=$'\e[0m'           # end underline
export LESS_TERMCAP_us=$'\e[04;38;5;146m' # begin underline


# For FZF
export FZF_DEFAULT_COMMAND='ag --hidden -g ""'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm


whoisusingthisport () { # check who is using the port
    lsof -i $1
}
