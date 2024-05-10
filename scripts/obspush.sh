#!/usr/bin/env bash
# This needn't be a script, but I want to have such files centralized for easier 
# adjustments, and potential expansion of the script (e.g. with)
cd ~/gdrive/Obsidian && git add .
git commit -m "Update obsidian"
git push
cd -