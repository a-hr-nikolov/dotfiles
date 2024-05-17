#!/usr/bin/env bash
# A script to start specific apps on specific KDE virtual desktops. Basically trying to
# mimic a tiling window manager startup. 
#
# To extend the script make sure to set appropriate sleep timers after each program.
# That is because some apps are really slow to start and if you know a specific app is
# like that, add some sleep after launching. That way the block for the next app in line
# doesn't have to include sleep time related to the previous app.
#
# Although much of this functionality can be achieved by KDE itself, I've found that it
# isn't as flexible, especially when it comes to opening profiled apps at specific
# virtual desktops. 
#
# That being said if you don't have such usecases, it's probably best to stick with 
# KDE's autostart settings in System Settings > System > Autostart.

# Switch to desktop X
switch_to_desktop() {
    desktop_number="$1"
    qdbus6 org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut "Switch to Desktop $desktop_number"
}

### Loading a Facebook (Messenger) and Gmail PWAs (through Vivaldi)
### Alternatively, they can be 
switch_to_desktop 1  # in case someone runs it directly
sleep 3  # Necessary due to bootup taking some time.
/opt/vivaldi/vivaldi --profile-directory=Default --app-id=kippjfofjhjlffjecoapiogbkgbpmgej &  # Messenger
sleep 1
vivaldi --profile-directory=Default &
firefox &
sleep 3

### Work Profile
switch_to_desktop 2
google-chrome --profile-directory="Profile 2" & disown
sleep 2

### END OF CHAIN
# Optionally, you may stay on the desktop with the last app open.
switch_to_desktop 1