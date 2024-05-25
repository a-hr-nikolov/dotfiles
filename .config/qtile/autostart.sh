#!/usr/bin/env bash

COLORSCHEME=DoomOne

### AUTOSTART PROGRAMS ###
picom --daemon & disown

# KDE SERVICES
kdeinit5 & disown
kded6 & disown
/usr/libexec/polkit-kde-authentication-agent-1 & 
kwalletd6 &

nm-tray & disown
# conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
