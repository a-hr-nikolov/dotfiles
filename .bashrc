# Sample .bashrc for SUSE Linux
# Copyright (c) SUSE Software Solutions Germany GmbH

# There are 3 different types of shells in bash: the login shell, normal shell
# and interactive shell. Login shells read ~/.profile and interactive shells
# read ~/.bashrc; in our setup, /etc/profile sources ~/.bashrc - thus all
# settings made here will also take effect in a login shell.
#
# NOTE: It is recommended to make language settings in ~/.profile rather than
# here, since multilingual X sessions would not work properly if LANG is over-
# ridden in every subshell.

test -s ~/.alias && . ~/.alias || true
eval "$(starship init bash)"

########################################################################################
# Aliases 
########################################################################################

# Zypper
alias zypin='sudo zypper install'
alias zypse='zypper se'
alias zypup='sudo zypper ref && sudo zypper dup'
alias zyprm='sudo zypper remove'

# List command
alias ls='eza -Al --color=always --group-directories-first' # my preferred listing
alias ll='eza -l --color=always --group-directories-first'  # long format
alias lt='eza -aT --color=always --group-directories-first' # tree listing

# Python Aliases
alias py='python3'
alias djm='python3 manage.py'

# Google Drive Sync aliases
alias drivepush='rclone sync ~/gdrive/Obsidian drive:--Obsidian'
alias drivepull='rclone sync drive:--Obsidian ~/gdrive/Obsidian'

# navigation
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# adding flags
alias df='df -h'               # human-readable sizes
alias free='free -m'           # show sizes in MB
alias grep='grep --color=auto' # colorize output (good for log files)
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# change your default USER shell
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Log out and log back in for change to take effect.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Log out and log back in for change to take effect.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Log out and log back in for change to take effect.'"