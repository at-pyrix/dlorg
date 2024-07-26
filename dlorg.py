import shutil
import os
import argparse
from pathlib import Path
from colorama import Fore as fc, Back as bg, init
import magic

init(autoreset=True)

folder_names = {
    "Audio": {'8svx', 'aac', 'ac3', 'aiff', 'amb', 'au', 'avr', 'caf', 'cdda', 'cvs', 'cvsd', 'cvu', 'dts', 'dvms', 'fap', 'flac', 'fssd', 'gsrt', 'hcom', 'htk', 'ima', 'ircam', 'm4a', 'm4r', 'maud', 'mp2', 'mp3', 'nist', 'oga', 'ogg', 'opus', 'paf', 'prc', 'pvf', 'ra', 'sd2', 'sln', 'smp', 'snd', 'sndr', 'sndt', 'sou', 'sph', 'spx', 'tta', 'txw', 'vms', 'voc', 'vox', 'w64', 'wma', 'wv'},
    "Archive": {'7z', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip', 'tar.bz2', 'tar.xz', 'gz', 'bz2', 'xz'},
    'Code': {'c', 'class', 'cpp', 'cs', 'css', 'go', 'h', 'htaccess', 'html', 'java', 'js', 'json', 'kml', 'php', 'pl', 'py', 'rb', 'sql', 'swift', 'vb', 'yaml'},
    'Documents': {'csv', 'djvu', 'doc', 'docx', 'odp', 'ods', 'odt', 'ott', 'pdf', 'ppt', 'rtf', 'txt', 'xls', 'xlsx', 'md'},
    'Ebooks': {'azw3', 'epub', 'fb2', 'lrf', 'mobi', 'pdb', 'snb'},
    'Images': {'bmp', 'cr2', 'cur', 'dds', 'dng', 'erf', 'exr', 'fts', 'gif', 'hdr', 'heic', 'heif', 'ico', 'jfif', 'jp2', 'jpe', 'jpeg', 'jpg', 'jps', 'mng', 'nef', 'nrw', 'orf', 'pam', 'pbm', 'pcd', 'pcx', 'pef', 'pes', 'pfm', 'pgm', 'picon', 'pict', 'png', 'pnm', 'ppm', 'psd', 'raf', 'ras', 'rw2', 'sfw', 'sgi', 'svg', 'tga', 'tiff', 'wbmp', 'webp', 'wpg', 'x3f', 'xbm', 'xcf', 'xpm', 'xwd'},
    'Programs': {'apk', 'bin', 'jar', 'msi', 'exe', 'appimage', 'run', 'sh', 'fish'},
    'Videos': {'3gp', 'asf', 'avi', 'f4v', 'flv', 'hevc', 'm2ts', 'm2v', 'm4v', 'mjpeg', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'mxf', 'ogv', 'rm', 'swf', 'ts', 'vob', 'webm', 'wmv'},
    'Fonts': {'cff', 'dfont', 'otf', 'pfb', 'ps', 'sfd', 'ttf', 'woff'}
}

folder_icons = {
    "Audio": "folder-music",
    "Archive": "default-folder-tar",
    "Code": "folder-development",
    "Documents": "folder-documents",
    "Ebooks": "folder-book",
    "Images": "folder-images",
    "Programs": "folder-script",
    "Videos": "folder-videos",
    "Fonts": "folder-activities"
}

xdg_download_dir = os.getenv('XDG_DOWNLOAD_DIR', '~/Downloads')
folder = Path(xdg_download_dir).expanduser()

if not folder.exists():
    print(bg.RED + 'ERR' + bg.RESET + ' ' + 'Folder Does Not Exist')
    exit(1)

def find_category(file):
    extension = file.suffix[1:].casefold() if file.suffix else "NONE"
    category = None

    # Check by file extension
    for key, value in folder_names.items():
        if extension in value:
            category = key
            break

    # Check by MIME type if category wasn't found by extension
    if category is None:
        mime_type = magic.from_file(str(file), mime=True)
        if mime_type:
            if mime_type.startswith('audio/'):
                category = 'Audio'
            elif mime_type.startswith('video/'):
                category = 'Videos'
            elif mime_type.startswith('image/'):
                category = 'Images'
            elif mime_type.startswith('text/'):
                category = 'Documents'
            elif mime_type.startswith('application/'):
                if 'pdf' in mime_type:
                    category = 'Documents'
                elif 'x-python' in mime_type or 'x-shellscript' in mime_type:
                    category = 'Code'
                elif 'x-font' in mime_type:
                    category = 'Fonts'

    return category

def create_directory_file(category_path, category):
    icon = folder_icons.get(category, "folder")
    directory_file_content = f"[Desktop Entry]\nIcon={icon}\n"
    directory_file_path = category_path / '.directory'
    with open(directory_file_path, 'w') as f:
        f.write(directory_file_content)

def sort_files():
    sort_flag = False
    for item in folder.iterdir():
        if item.is_dir() or item.name.startswith('.'):
            continue

        sort_flag = True

        category = find_category(item)
        if category:
            category_path = folder / category
            if not category_path.exists():
                category_path.mkdir()
                create_directory_file(category_path, category)

            try:
                moved_path = shutil.move(str(item), str(category_path))
                print(f"{fc.CYAN}Moved {fc.RESET}{item.name}{fc.LIGHTBLACK_EX} to {fc.CYAN}{category}{fc.RESET}")
            except shutil.Error as e:
                print(bg.RED + 'ERR' + bg.RESET + ' ' + str(e))
        else:
            print(f"{fc.YELLOW}Left {fc.RESET}{item.name}{fc.LIGHTBLACK_EX} {fc.YELLOW}in Downloads{fc.RESET}")

    if not sort_flag:
        print("There is nothing to do.")

def main():
    parser = argparse.ArgumentParser(description='Sort your downloads folder by file extensions.')
    args = parser.parse_args()
    sort_files()

if __name__ == '__main__':
    main()
