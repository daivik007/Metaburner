#!/bin/bash

FONT_FOLDER="$(dirname "$(realpath "$0")")/Fonts"
FONT_DEST="$HOME/.local/share/fonts"

# Function to pause before exiting
pause_and_exit() {
    echo -e "\nPress ENTER to exit..."
    read
    exit
}

# Check if font folder exists
if [ ! -d "$FONT_FOLDER" ]; then
    echo -e "\033[0;31m❌ Font folder not found: $FONT_FOLDER\033[0m"
    pause_and_exit
fi

# Create destination folder if it doesn't exist
mkdir -p "$FONT_DEST"

# Copy fonts
echo "Installing fonts to $FONT_DEST..."
find "$FONT_FOLDER" -type f -name "*.otf" -exec cp "{}" "$FONT_DEST" \;

# Refresh font cache
fc-cache -f "$FONT_DEST"

echo -e "\033[0;32m✅ Fonts installed successfully!\033[0m"

pause_and_exit
