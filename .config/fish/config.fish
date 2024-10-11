########################################################################################
# ENV Variables / EXPORTs
########################################################################################

set fish_greeting                                 # Supresses fish's intro message
set -x LANG en_US.UTF-8
# set -x LC_ALL en_US.UTF-8
set -x PAGER less
set -x EDITOR /usr/bin/code
set -x PATH $PATH $HOME/go/bin
# set -x TERM xterm-256color  # uncomment if some programs have issues with the emulator

# For KVM
set -x LIBVIRT_DEFAULT_URI qemu:///system

# Set up fzf key bindings
fzf --fish | source

########################################################################################
# FUNCTIONS 
########################################################################################

# Functions needed for !! and !$
function __history_previous_command
    switch (commandline -t)
    case "!"
        commandline -t $history[1]; commandline -f repaint
    case "*"
        commandline -i !
    end
end

function __history_previous_command_arguments
    switch (commandline -t)
    case "!"
        commandline -t ""
        commandline -f history-token-search-backward
    case "*"
        commandline -i '$'
    end
end

# The bindings for !! and !$
if [ "$fish_key_bindings" = "fish_vi_key_bindings" ];
    bind -Minsert ! __history_previous_command
    bind -Minsert '$' __history_previous_command_arguments
else
    bind ! __history_previous_command
    bind '$' __history_previous_command_arguments
end

# Function for copying files and directories, even recursively.
# ex: copy DIRNAME LOCATIONS
# result: copies the directory and all of its contents.
function copy
    set count (count $argv | tr -d \n)
    if test "$count" = 2; and test -d "$argv[1]"
	set from (echo $argv[1] | trim-right /)
	set to (echo $argv[2])
        command cp -r $from $to
    else
        command cp $argv
    end
end

########################################################################################
# Starship 
########################################################################################

# Starship prompt setup
starship init fish | source


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
alias python='python3'
alias djm='python3 manage.py'
alias prun='poetry run'
alias ppy='poetry run python'
alias ppm='poetry run python manage.py'

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
alias df='df -h'                # human-readable sizes
alias du='du -h'
alias free='free -m'            # show sizes in MB
alias grep='grep --color=auto'  # colorize output (good for log files)
alias cp='cp -i'                # makes potentially destructive commands require confirmation
alias mv='mv -i'
alias rm='rm -i'

# change your default USER shell
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Log out and log back in for change to take effect.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Log out and log back in for change to take effect.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Log out and log back in for change to take effect.'"

# grep and rgrep
alias grepls="grep -lrS"    # returns the files that simply include the pattern
alias rg="rg -S"            # smartcase search
alias rgls="rg -lrS"

# searching aliases
alias fcmd="history | fzf"
alias fman="compgen -c | fzf | xargs man"  # actually doesn't work in fish

# utils
alias fbig="du -ah . | sort -hr | head -n 30"  # gets disk usage, sorts it in reverse, prints the first 30
alias bye="sudo shutdown -h now"

# dict
alias dict="/home/anikolov/repos/en-bg-dict/.venv/bin/python /home/anikolov/repos/en-bg-dict/en_bg_dict/main.py"
