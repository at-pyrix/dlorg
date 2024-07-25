import os
import shutil
import time
import ntpath
import argparse
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from colorama import Fore as fc, Back as bg, init
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

folder = str(Path("~/Downloads").expanduser())

if folder.endswith('/'):
    folder = folder[:-1]
if not os.path.exists(folder):
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
        full_path = os.path.join(folder, filename)
        if os.path.isdir(full_path) or filename.startswith('.'):
            continue

        sort_flag = True

        category = find_category(filename)
        if not os.path.exists(f'{folder}/{category}'):
            os.mkdir(f'{folder}/{category}')

        try:
            moved_path = shutil.move(full_path, f'{folder}/{category}')
            print(fc.LIGHTBLACK_EX + str(datetime.now()) + fc.GREEN + ' File moved to: ' + fc.RESET + moved_path)
        except shutil.Error as e:
            print(bg.RED + 'ERR' + bg.RESET + ' ' + str(e))

    if not sort_flag: print("There is nothing to do.")

class OnFileChange:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, folder, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print(fc.RED + "Script Terminated")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        filename = ntpath.basename(event.src_path)
        if event.is_directory:
            return None
        elif event.event_type == 'created' and '.part' not in filename and '.crdownload' not in filename and not filename.startswith('.'):
            time.sleep(0.5)
            print(fc.LIGHTBLACK_EX + str(datetime.now()) + fc.GREEN + ' New download detected: ' + fc.RESET + event.src_path)
            category = find_category(filename)
            if not os.path.exists(f'{folder}/{category}'):
                os.mkdir(f'{folder}/{category}')
            try:
                full_path = shutil.move(event.src_path, f'{folder}/{category}')
            except shutil.Error as e:
                print(bg.RED + 'ERR' + bg.RESET + ' ' + str(e))
                return
            print(fc.LIGHTBLACK_EX + str(datetime.now()) + fc.GREEN + ' Download moved to: ' + fc.RESET + full_path)

def main():
    parser = argparse.ArgumentParser(description='Sort your downloads folder by file extensions.')
    parser.add_argument('--watch', action='store_true', help='Watch the downloads folder for new files.')
    args = parser.parse_args()

    if args.watch:
        print('Watching Downloads Folder...\n')
        watch = OnFileChange()
        watch.run()
    else:
        sort_files()

if __name__ == '__main__':
    main()
