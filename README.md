# Metaburner

**Metaburner** is a streamlined Python-based tool designed to burn subtitles into video files effortlessly. It leverages FFmpeg and `ffmpeg-progressbar-cli` to provide a clean, user-friendly experience with real-time progress updates.

## Features

- 🎞️ **Subtitle Burning**: Seamlessly embeds subtitles into video files.
- 📁 **Output Folder Selection**: Choose your desired output directory for processed videos.
- 🔄 **Optional Subtitle Conversion**: Convert subtitle formats as needed.
- 🆎 **Custom Font Support**: Utilizes the **Netflix Sans** font for subtitles, ensuring readability.
- 📊 **Progress Bar**: Displays a clean progress bar with estimated time remaining.
- 🧹 **Minimal Logging**: Suppresses verbose FFmpeg logs for a cleaner output.

## Prerequisites

Ensure you have the following installed on your system:

- **Python**: [Download Python](https://www.python.org/downloads/)

## Installation

### Standard Manual Installation (Windows):

1. Clone the repository:

   ```bash
   git clone https://github.com/daivik007/Metaburner.git
   cd Metaburner
   ```

2. Install the required packages:

   - Run the setup script to install necessary dependencies:

   ```bash
   setup_dependencies.bat
   ```

   - Install Netflix Sans font (via Powershell 7 as Admin) from `install_font.ps1`

## Usage

Run **Metaburner**:

```
python metaburner.py
```

## File Structure

```
Metaburner/
│
├── Fonts/                             # Directory containing NetflixSans.otf font files
│   └── NetflixSans-Medium.otf
│
├── node_modules/                      # Created after npm install (gitignored)
│
├── .gitignore                         # Specifies untracked files to ignore
├── install_fonts.ps1                  # PowerShell script to install fonts (Windows)
├── install_fonts.sh                   # Font installer script (Linux)
├── LICENSE                            # MIT License
├── metaburner.py                      # Main script to handle subtitle burning
├── package.json                       # Node.js config (for ffmpeg-progressbar-cli)
├── package-lock.json                  # Locks npm dependency versions
├── README.md                          # Project documentation
├── setup_dependencies.bat             # Dependency setup for Windows
└── setup_dependencies.sh              # Dependency setup for Linux
```

## Contributing

Feel free to submit issues or pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
