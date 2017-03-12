# START bash_profile -DO-NOT-EDIT
# grep with color
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

alias iconf='cd ~/projects/iconfigs'
alias activate_here='source .*/bin/activate 2> /dev/null || source */bin/activate 2> /dev/null'
alias saltme='sudo salt-call --local state.apply iconfigs'
alias t='python manage.py test'

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
# END bash_profile
