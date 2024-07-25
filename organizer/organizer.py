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
    "Audio": {'8svx', 'aac', 'ac3', 'aiff', 'amb', 'au', 'avr', 'caf', 'cdda', 'cvs', 'cvsd', 'cvu', 'dts', 'dvms', 'fap', 'flac', 'fssd', 'gsrt', 'hcom', 'htk', 'ima', 'ircam', 'm4a', 'm4r', 'maud', 'mp2', 'mp3', 'nist', 'oga', 'ogg', 'opus', 'paf', 'prc', 'pvf', 'ra', 'sd2', 'sln', 'smp', 'snd', 'sndr', 'sndt', 'sou', 'sph', 'spx', 'tta', 'txw', 'vms', 'voc', 'vox', 'w64', 'wma', 'wv'},

    "Archive": {'7z', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip', 'tar.bz2', 'tar.xz', 'gz', 'bz2', 'xz'},

    'Code': {'c', 'class', 'cpp', 'cs', 'css', 'go', 'h', 'htaccess', 'html', 'java', 'js', 'json', 'kml', 'php', 'pl', 'py', 'rb', 'sql', 'swift', 'vb', 'yaml'},

    'Documents': {'csv', 'djvu', 'doc', 'docx', 'odp', 'ods', 'odt', 'ott', 'pdf', 'ppt', 'rtf', 'txt', 'xls', 'xlsx'},

    'Ebooks': {'azw3', 'epub', 'fb2', 'lrf', 'mobi', 'pdb', 'snb'},

    'Images': {'bmp', 'cr2', 'cur', 'dds', 'dng', 'erf', 'exr', 'fts', 'gif', 'hdr', 'heic', 'heif', 'ico', 'jfif', 'jp2', 'jpe', 'jpeg', 'jpg', 'jps', 'mng', 'nef', 'nrw', 'orf', 'pam', 'pbm', 'pcd', 'pcx', 'pef', 'pes', 'pfm', 'pgm', 'picon', 'pict', 'png', 'pnm', 'ppm', 'psd', 'raf', 'ras', 'rw2', 'sfw', 'sgi', 'svg', 'tga', 'tiff', 'wbmp', 'webp', 'wpg', 'x3f', 'xbm', 'xcf', 'xpm', 'xwd'},

    'Programs': {'apk', 'bin', 'jar', 'msi', 'exe', 'appimage', 'run'},

    'Videos': {'3gp', 'asf', 'avi', 'f4v', 'flv', 'hevc', 'm2ts', 'm2v', 'm4v', 'mjpeg', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'mxf', 'ogv', 'rm', 'swf', 'ts', 'vob', 'webm', 'wmv'},

    'Fonts': {'cff', 'dfont', 'otf', 'pfb', 'ps', 'sfd', 'ttf', 'woff'},

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
