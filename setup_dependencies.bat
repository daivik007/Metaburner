@echo off

echo Installign Node.js and npm...
winget install OpenJS.NodeJS

echo Installing FFmpeg using winget...
winget install -e --id Gyan.FFmpeg

echo Installing ffmpeg-progressbar-cli globally with npm...
npm install --global ffmpeg-progressbar-cli

echo All dependencies installed!
pause
