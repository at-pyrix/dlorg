import os
import shutil
import time
import argparse
from datetime import datetime
from pathlib import Path
from colorama import Fore as fc, Back as bg, init
import platform

init(autoreset=True)

folder_names = {
    "Audio": {'aif', 'cda', 'mid', 'midi', 'mp3', 'mpa', 'ogg', 'wav', 'wma', 'flac', 'alac', 'aac', 'm4a'},
    "Archive": {'7z', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip', 'tar.bz2', 'tar.xz', 'gz', 'bz2', 'xz'},
    'Code': {'js', 'jsp', 'html', 'ipynb', 'py', 'java', 'css', 'c', 'cpp', 'cs', 'php', 'rb', 'rs', 'go', 'pl', 'r', 'swift', 'ts', 'sql', 'json', 'yaml', 'xml'},
    'Documents': {'ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'doc', 'docx', 'txt', 'tex', 'epub', 'odt', 'ods', 'odp', 'rtf', 'md', 'csv'},
    'Images': {'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'jfif', 'svg', 'tif', 'tiff', 'webp', 'heic', 'heif', 'raw', 'psd', 'ai', 'eps'},
    'Programs': {'apk', 'bat', 'bin', 'jar', 'msi', 'exe', 'appimage', 'run', 'sh'},
    'Videos': {'3gp', 'avi', 'flv', 'h264', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'wmv', 'webm', 'vob', 'm4v', 'divx', 'xvid'},
    'Fonts': {'ttf', 'otf', 'woff', 'woff2', 'eot', 'pfa', 'pfb'},
    'Others': {'NONE'}
}

# Determine the appropriate downloads folder path based on the operating system
if platform.system() == 'Windows':
    folder = Path(os.getenv('USERPROFILE', '')).joinpath('Downloads')
else:
    folder = Path("~/Downloads").expanduser()

if not folder.exists():
    print(bg.RED + 'ERR' + bg.RESET + ' ' + 'Folder Does Not Exist')
    exit(1)

def find_category(file):
    extension = file.split(".")[-1] if not file.startswith('.') else "NONE"
    category = "Others"

    for key, value in folder_names.items():
        if extension in value:
            category = key
            break

    return category

def sort_files():
    sort_flag = False
    for filename in os.listdir(folder):
        full_path = folder.joinpath(filename)
        if os.path.isdir(full_path) or filename.startswith('.'):
            continue

        sort_flag = True

        category = find_category(filename)
        category_path = folder.joinpath(category)
        if not category_path.exists():
            category_path.mkdir()

        try:
            moved_path = shutil.move(str(full_path), str(category_path))
            print(fc.LIGHTBLACK_EX + str(datetime.now()) + fc.GREEN + ' File moved to: ' + fc.RESET + moved_path)
        except shutil.Error as e:
            print(bg.RED + 'ERR' + bg.RESET + ' ' + str(e))

    if not sort_flag:
        print("There is nothing to do.")

def main():
    parser = argparse.ArgumentParser(description='Sort your downloads folder by file extensions.')
    args = parser.parse_args()
    sort_files()

if __name__ == '__main__':
    main()
