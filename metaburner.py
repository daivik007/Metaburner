import os
import re
import shutil
import subprocess
import sys

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def rename_and_copy():
    input_folder = input("\nEnter the input folder path: ").strip()
    output_folder = input("Enter the output folder path: ").strip()

    if not os.path.isdir(input_folder):
        print("❌ Invalid input folder path.\n")
        return

    os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    files.sort(key=natural_sort_key)

    if not files:
        print("⚠️ No files found in the input folder.\n")
        return

    for index, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]
        new_filename = f"ep{index}{file_ext}"

        src_path = os.path.join(input_folder, filename)
        dst_path = os.path.join(output_folder, new_filename)

        shutil.copy2(src_path, dst_path)
        print(f"✅ {filename} -> {new_filename}")

    print("\n✅ All files have been renamed and copied successfully!\n")

def get_npm_global_path():
    try:
        npm_path = subprocess.check_output(["npm.cmd","config","get","prefix"]).decode().strip()
        return npm_path
    except Exception:
        return None
    
def check_ffmpeg_bar_installed():
    npm_path = get_npm_global_path()
    if not npm_path:
        print("❌ Unable to fetch npm global path.")
        return False
    
    ffmpeg_bar_path = os.path.join(npm_path,"node_modules", "ffmpeg-progressbar-cli")
    if os.path.exists(ffmpeg_bar_path) and os.path.isdir(ffmpeg_bar_path):
        return True   
    else:
        print("❌ 'ffmpeg-progressbar-cli' (ffmpeg-bar) is not installed or not in PATH.")
        print("👉 Install it using: npm install -g ffmpeg-progressbar-cli\n")
        return False

def fix_path_for_ffmpeg(path):
    path = path.replace("\\", "/")
    fixed_path = re.sub(r'^([A-Za-z]):/', r'\1\\:/', path)
    return fixed_path

def burn_subtitles():
    print("\n--- Burn Subtitles to Video ---")

    if not check_ffmpeg_bar_installed():
        return

    video_file = input("Enter the path to the video file: ").strip()
    if not os.path.isfile(video_file):
        print("❌ Video file not found!\n")
        return

    subtitle_file = input("Enter the path to the subtitle file (.srt or .ass): ").strip()
    if not os.path.isfile(subtitle_file):
        print("❌ Subtitle file not found!\n")
        return

    output_folder = input("Enter the output folder path: ").strip()
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    video_dir, video_name = os.path.split(video_file)
    base_name, _ = os.path.splitext(video_name)
    output_file = os.path.join(output_folder, f"{base_name}_burned.mp4")

    video_file_fixed = video_file.replace("\\", "/")
    subtitle_file_fixed = fix_path_for_ffmpeg(subtitle_file)

    _, ext = os.path.splitext(subtitle_file)
    ext = ext.lower()

    if ext == '.ass':
        subtitle_filter = f"ass='{subtitle_file_fixed}:force_style='FontName=Netflix Sans Med,FontSize=22,PrimaryColour=&H00FFFFFF,Alignment=2,Shadow=1'"
    else:
        subtitle_filter = f"subtitles='{subtitle_file_fixed}':force_style='FontName=Netflix Sans Med,FontSize=22,PrimaryColour=&H00FFFFFF,Alignment=2,Shadow=1'"

    print("\n🔥 Burning subtitles... This may take a while.")

    print(f"\n🛠 Running command:\nffmpeg-bar -i \"{video_file_fixed}\" -vf \"{subtitle_filter}\" -c:v libx264 -preset slow -crf 16 -c:a copy \"{output_file}\"\n")

    process = subprocess.run(
        f'ffmpeg-bar -i "{video_file_fixed}" -vf "{subtitle_filter}" -c:a copy -y "{output_file}"',
        shell=True,
        stdout=sys.stdout, stderr=sys.stderr
    )
    print(process.stdout)

    if process.returncode == 0:
        print(f"\n✅ Subtitles burned successfully. Output file: {output_file}\n")
    else:
        print("\n❌ Failed to burn subtitles. Check your ffmpeg installation or subtitle format.\n")


def main():
    while True:
        print("\n===== 🔥 MetaBurner 🔥 =====")
        print("1. 📁 Rename media files (ep1, ep2...)")
        print("2. 🔥 Burn subtitles to media")
        print("3. ❌ Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            rename_and_copy()
        elif choice == '2':
            burn_subtitles()
        elif choice == '3':
            print("\n👋 Exiting MetaBurner. Have a great day!\n")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()


#FIXED: Error for ffmpeg main installed
#FIXED: Make conversion lossless
#FIXED: ffmpeg font like Netflix EXACT
#FIXED: Convert batch file to .ps1 file for windows powershell

#UPDATE: Add upscaling feature
#UPDATE: Add filetype conversion feature
#UPDATED: Make a requirements.txt file so that external libraries can be downloaded
#UPDATE: Docker integration

#FIXED: Make a proper .gitignore file so that the .git folder is not uploaded to the repo

