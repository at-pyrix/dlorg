# Download Organizer

A Python script to organize your downloads folder by file extensions. It can also watch the folder for new files and automatically sort them.

## Installation

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

### Custom Downloads Folder

If your downloads folder is different from the default (`~/Downloads`), update the `folder` variable in `organizer.py` to the desired path.

## Running the Script at System Startup (Linux)

To ensure the `--watch` script runs automatically at system startup, follow these steps:

1. **Create a Systemd Service File**

    Create a new service file for your script. Open a terminal and use a text editor to create a file in the `/etc/systemd/system/` directory:

    ```sh
    sudo nano /etc/systemd/system/download-organizer.service
    ```

    Add the following content to the file:

    ```ini
    [Unit]
    Description=Download Organizer Service
    After=network.target

    [Service]
    ExecStart=/usr/bin/dlorg --watch
    Restart=always
    User=yourusername
    Environment="PATH=/usr/bin:/usr/local/bin"

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `yourusername` with your actual username.

2. **Reload Systemd Daemon**

    After creating the service file, reload the systemd daemon to recognize the new service:

    ```sh
    sudo systemctl daemon-reload
    ```

3. **Enable the Service**

    Enable the service so that it starts automatically on boot:

    ```sh
    sudo systemctl enable download-organizer.service
    ```

4. **Start the Service**

    Start the service immediately without rebooting:

    ```sh
    sudo systemctl start download-organizer.service
    ```

5. **Check the Status**

    Verify that the service is running:

    ```sh
    sudo systemctl status download-organizer.service
    ```

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
