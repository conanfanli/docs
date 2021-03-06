# This is for {{rice_type}}
RED='\033[1;31m'
NO_COLOR='\033[0m' # No Color

yell() { # echo with color
    echo -e "\n[+] ${RED}$@${NO_COLOR}"
}

if [ -f ~/bin/z.sh ]
then
    . ~/bin/z.sh
fi
alias tmux='tmux -2u'

export PATH=$PATH:$HOME/bin
export HISTFILESIZE=5000
# export LC_ALL=en_US.UTF-8
# export LANG=en_US.UTF-8
# export LANGUAGE=en_US.UTF-8
export EDITOR=vim

{% if ansible_os_family == 'Darwin' %}
# For MAC
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

{% if rice_type == 'bash' %}
# source bash_completion if the current shell is bash
. $(brew --prefix)/etc/bash_completion
{% endif %}

alias ls='ls -GFh'
{% else %}
alias ls='ls -GFh --color'
# END MAC
{% endif %}

{% if rice_type == 'bash' %}
# These only apply to bash
LS_COLORS="ow=01;96:di=01;96" ; export LS_COLORS
PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$\n% "
alias so='source ~/.bashrc' #desc#: re-source ~/.bashrc
{% else %}
alias so='source ~/.zshrc' #desc#: re-source ~/.zshrc
{% endif %}


# linux commands
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -FGlAhp'
alias la='ls -a'
alias ..='cd ../'
alias ...='cd ../../'

# Personal projects, shortcuts
alias iconf='cd ~/projects/iconfigs'


git-clone() {
    git clone git@github.com:conanfanli/$1.git
    cd $1
    git smart-config
}

yank() { # drop in dropbox
    (cd ~/dropbox/ &&  echo $1 > ~/dropbox/yanked && \
        git add -A && git commit -m 'paste yanked'&& git push)
}

wank() { # paste what was yanked
    (cd ~/dropbox/ &&  git pull > /dev/null && cat ./yanked)
}

hub () { # open the repo in github
    URL="https://github.com/$(git remote get-url origin | ag '(?<=:)(.*?)(?=\.git)' -o)"
    open $URL
}

fdir () { # Find directory matching pattern
    find . -type d -name $@ -print
}

alias myip='curl https://ifconfig.co/'  # print my IP address

cmds () { # show all aliases and functions in a list
    selected=`~/rice/cooker-proj/commandos/get_all_aliases.py | fzf | ag -o '^(.*)(?=:)'`
    read -p "$selected " args

    eval "$selected $args"
}

v () { # activate virtualenv if there is one
    base=`basename $PWD`
    name=${1-$base}
    . ~/envs/$name/bin/activate 2> /dev/null || echo Available envs: `ls ~/envs`
    [ -f "./.postactivate" ] && . .postactivate
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

pro() {
    lineno=`wc -l < ~/rice/commits.txt`
    message=`head -$((${RANDOM} %  $lineno + 1)) ~/rice/commits.txt  | tail -1`
    ci $message
}

gdm () { # delete stale branches
    git branch --merged | grep -v '*' | xargs git branch -d
    git fetch -p
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
push() { # git push branch even when the current branch has no upstream branch
    cmd_to_set_upstream=`git push 2>&1 | grep 'git push.*' -o`
    [ -n "$cmd_to_set_upstream" ] && $cmd_to_set_upstream
}

alias dockerclean='(docker ps -aq | xargs docker rm); (docker images -aq -f dangling=true | xargs docker rmi); docker volume rm $(docker volume ls -qf dangling=true)'  # clean up docker containers and volumnes
alias dc='docker-compose' # shorcut to docker-compose
alias disk-space='df -h'  # Display disk space usage

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


whoisusingthisport () { # check who is using the port
    lsof -t -i $1
}

export BASH_SILENCE_DEPRECATION_WARNING=1

