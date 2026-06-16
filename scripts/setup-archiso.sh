#!/bin/bash
# NexusWins - archiso setup script

echo "Setting up NexusWins build environment..."

# Install archiso
sudo pacman -S --noconfirm archiso

# Copy the baseline profile
cp -r /usr/share/archiso/configs/releng/ ~/nexuswins-profile

echo "Done! Profile created at ~/nexuswins-profile"