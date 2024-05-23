# Stuff that should be run only once for OpenSUSE.
# I am transitioning to Nix, so this will eventually turn into a config, which is why I 
# am not bothering to make it a true setup script.

# Prerequisites:
#   - libvirt (zypper in -t pattern kvm_server kvm_tools; zypper in libvirt)
#   - openrazer

# sudo systemctl start libvirtd  # this is to start it once after installing
sudo systemctl enable libvirtd