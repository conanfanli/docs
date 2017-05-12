# START bash_profile -DO-NOT-EDIT
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
export HISTFILESIZE=2000
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8

# For MAC
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
if which brew 2> /dev/null && [ -f $(brew --prefix)/etc/bash_completion ]
then
    . $(brew --prefix)/etc/bash_completion
    alias ls='ls -GFh'
else
    alias ls='ls -GFh --color'
fi

# END MAC


# grep with color
alias vim='~/bin/vim'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -l'
alias la='ls -a'

alias docs='cd ~/docs'
alias iconf='cd ~/projects/iconfigs'
alias activate_here='source .*/bin/activate 2> /dev/null || source */bin/activate 2> /dev/null'
alias saltme='sudo salt-call --local state.apply iconfigs'
alias t='python manage.py test'
alias so='source ~/.bash_profile'
alias sag='eval `ssh-agent` && ssh-add ~/.ssh/id_rsa'

v () {
    base=`basename $PWD`
    name=${1-$base}
    . ~/envs/$name/bin/activate 2> /dev/null || echo Available envs: `ls ~/envs`
}

ci () {
    ticket=`git branch | grep '*' |grep 'JUMP-[0-9]*' -o`
    read -p "You better come up with some thing good to say: " message
    if [ -n "$ticket" ]; then
        git commit -a -m "$ticket: $message"
    else
        git commit -a -m "$message"
    fi
}

gdm () {
    git branch --merged | grep -v '*' | xargs git branch -d
    git fetch -p
}

clip () {
    echo "$1" > /usr/share/nginx/html/clips/1.txt
}

alias dockerclean='(docker ps -aq | xargs docker rm); (docker images -aq -f dangling=true | xargs docker rmi); docker volume rm $(docker volume ls -qf dangling=true)'
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

LS_COLORS="ow=01;96:di=01;96" ; export LS_COLORS
PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "

# For FZF
export FZF_DEFAULT_COMMAND='ag --hidden -g ""'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
# END bash_profile
