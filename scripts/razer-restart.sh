#/usr/bin/env bash  # deliberately not shebanged
#
# This "script" restarts the Razer mouse if it doesn't seem to get recognized by the
# openrazer daemon.
#
# Technically, it may not be working for a variety of reasons, so this isn't to be
# executed as a script. Rather it's more of a collection of commands that may or may not
# be run together.
#
# Check https://github.com/openrazer/openrazer/wiki/Troubleshooting for more info.
# https://www.reddit.com/r/SolusProject/comments/6x9tdv/razergenie_doesnt_detect_my_mouse/ 

pkill razer
openrazer-daemon # -Fv
sudo usbhid-dump -m 1532