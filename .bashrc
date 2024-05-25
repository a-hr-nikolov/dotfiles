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

# Starship integration
eval "$(starship init bash)"

# fzf - fuzzy finder integration
# Set up fzf key bindings and fuzzy completion
eval "$(fzf --bash)"

# Use go bin as part of path
export PATH=$PATH:~/go/bin

export LANG=en_US.UTF-8
# export LC_ALL=en_US.UTF-8
export HISTCONTROL=ignoreboth
export PAGER=less
export EDITOR=/usr/bin/code
# export TERM=xterm-256color

# For KVM
export LIBVIRT_DEFAULT_URI='qemu:///system'

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

# Obsidian Sync Aliases
alias obpushdrive='rclone sync ~/gdrive/Obsidian drive:obsidian'
alias obpulldrive='rclone sync drive:obsidian ~/gdrive/Obsidian'
alias obpushgit="~/dotfiles/scripts/obspush.sh"
alias obpushall="obpushdrive; obpushgit"

# navigation
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# adding flags
alias df='df -h'               # human-readable sizes
alias du='du -h'
alias free='free -m'           # show sizes in MB
alias grep='grep --color=auto' # colorize output (good for log files)
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# change your default USER shell
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Log out and log back in for change to take effect.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Log out and log back in for change to take effect.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Log out and log back in for change to take effect.'"
