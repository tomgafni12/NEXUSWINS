#!/bin/bash
# NexusWins - Wine Installation Script
# Windows app compatibility layer

echo "Installing Wine for NexusWins..."

# Enable multilib repo for 32-bit support
sudo sed -i "/\[multilib\]/,/Include/"'s/^#//' /etc/pacman.conf

# Install Wine and dependencies
sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm \
    wine \
    wine-mono \
    wine-gecko \
    winetricks \
    dxvk-bin \
    vkd3d

# Create NexusWins Wine prefix
mkdir -p ~/.nexuswins/wine
WINEPREFIX=~/.nexuswins/wine WINEARCH=win64 wineboot

echo "Wine installed successfully!"
echo "Test with: wine --version"