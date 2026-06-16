# NexusWins Build Plan

## Overview
NexusWins is built on Arch Linux using archiso to create 
a custom bootable ISO with pre-integrated compatibility layers.

## Base System
- Base: Arch Linux
- Build tool: archiso
- Package manager: pacman + yay (AUR)

## Compatibility Layers
| Layer | Purpose | Status |
|-------|---------|--------|
| Wine | Run Windows apps | Planned |
| Waydroid | Run Android apps | Planned |
| Darling | Run macOS apps | Planned |

## Build Process
1. Set up archiso profile
2. Add compatibility layer packages
3. Configure autostart and integration
4. Build ISO
5. Test in VirtualBox
6. Release

## Testing
- VirtualBox for development testing
- QEMU as backup
- Real hardware testing before any public release