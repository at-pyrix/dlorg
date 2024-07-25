# Download Organizer

A Python script to organize your downloads folder by file extensions. It can also watch the folder for new files and automatically sort them.

## Installation

> [!WARNING]
> If you get this error: `error: externally-managed-environment`, run the command `pip install . --break-system-packages` (this may break stuff)

### Using PIP

```
pip install download-organizer
```

### Manual

1. Clone the repository:

    ```sh
    git clone https://github.com/at-pyrix/download-organizer.git
    cd download-organizer
    ```

2. Install the dependencies and the CLI tool:

    ```sh
    pip install .
    ```

## Usage

### Manual Sorting

To sort your downloads folder manually, run:

```sh
dlorg
```

### Watching Downloads Folder

To watch the downloads folder and sort new files automatically, run:

```sh
dlorg --watch
```

## Running the script at startup (linux)

To ensure the `--watch` script runs automatically at system startup, follow these steps:

1. **Open Crontab for Editing**

   Open your crontab configuration file in edit mode:

   ```sh
   crontab -e
   ```

2. **Add an Entry to Run the Script at Startup**

   Add the following line to the crontab file to run the `dlorg` command at startup:

   ```sh
   @reboot ~/.local/bin/dlorg --watch
   ```

3. **Verify Crontab Entry**

   Ensure that the new entry is added to the crontab:

   ```sh
   crontab -l
   ```

### Custom Downloads Folder

If your downloads folder is different from the default (`~/Downloads`), update the `folder` variable in `organizer.py` to the desired path.

## Running the Script at System Startup (Linux)

## Folder Categories

The script sorts files into the following categories:

- **Audio**: aif, cda, mid, midi, mp3, mpa, ogg, wav, wma, flac, alac, aac, m4a
- **Archive**: 7z, deb, pkg, rar, rpm, tar.gz, z, zip, tar.bz2, tar.xz, gz, bz2, xz
- **Code**: js, jsp, html, ipynb, py, java, css, c, cpp, cs, php, rb, rs, go, pl, r, swift, ts, sql, json, yaml, xml
- **Documents**: ppt, pptx, pdf, xls, xlsx, doc, docx, txt, tex, epub, odt, ods, odp, rtf, md, csv
- **Images**: bmp, gif, ico, jpeg, jpg, png, jfif, svg, tif, tiff, webp, heic, heif, raw, psd, ai, eps
- **Programs**: apk, bat, bin, jar, msi, exe, appimage, run, sh
- **Videos**: 3gp, avi, flv, h264, mkv, mov, mp4, mpg, mpeg, wmv, webm, vob, m4v, divx, xvid
- **Fonts**: ttf, otf, woff, woff2, eot, pfa, pfb
- **Others**: any other file types


## License

This project is licensed under the GNU General Public License v3.0 - see the `LICENSE` file for details.
