#!/data/data/com.termux/files/usr/bin/bash

# Clear terminal screen
clear

# Color Palette for Installer UI
GREEN="\033[92m"
RED="\033[91m"
RESET="\033[0m"
BLUE="\033[94m"
YELLOW="\033[93m"
CYAN="\033[96m"

print_status() {
    echo -e "${CYAN}[*] $1...${RESET}"
}

echo -e "${GREEN}=================================================="
echo -e "       HCO-METAX SRY ENVIRONMENT INSTALLER            "
echo -e "              DEVELOPED BY: 𒉭 ᎠᴀʀᴋㅤᏙᴇɴᴏᴍㅤ×͜× | 𝐓𝐇𝐄 𝐀𝐋𝐏𝐇𝐀 𒉭              "
echo -e "==================================================${RESET}\n"

# Step 1: System Package Update
print_status "Updating Termux repositories and packages"
pkg update -y && pkg upgrade -y

# Step 2: Core Dependencies
print_status "Installing Python and Git ecosystem"
pkg install python git -y

# Step 3: Required Library for Image Processing
print_status "Installing Pillow compilation dependencies (libjpeg, zlib)"
pkg install libjpeg-turbo libtiff -y

# Step 4: Python Library Compilation
print_status "Compiling and installing Pillow package via pip"
pip install --upgrade pip
pip install pillow

# Step 5: Android Storage Optimization Request
print_status "Requesting Termux Android Storage Access Permissions"
termux-setup-storage

echo -e "\n${GREEN}[✓] Environment Successfully Configured!${RESET}"
echo -e "${YELLOW}[🚀] Run the tool using: ${RESET}${GREEN}python hco_metax.py${RESET}\n"
