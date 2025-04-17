#!/bin/bash

echo "Installing Node.js and npm..."
sudo apt update
sudo apt install -y nodejs npm

echo "Installing FFmpeg..."
sudo apt install -y ffmpeg

echo "Installing ffmpeg-progressbar-cli globally with npm..."
sudo npm install --global ffmpeg-progressbar-cli

echo -e "\n✅ All dependencies installed!"
echo -e "Press ENTER to exit..."
read
