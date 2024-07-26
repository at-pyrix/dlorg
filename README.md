<h1 align=center>Download Organizer ⬇️</h1>
<p align=center>
<img src="https://raw.githubusercontent.com/at-pyrix/dlorg/main/demo.gif"/>
</p>
<p align=center>A Python script to organize your downloads folder by file extensions and mimetypes.</p>

## Installation

### Using [pipx](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx) (recommended ✓)
```
pipx install dlorg
```

### Manual

1. Clone the repository:

    ```sh
    git clone https://github.com/at-pyrix/dlorg.git
    cd dlorg
    ```

2. Install the dependencies and the CLI tool:

    ```sh
    pipx install .
    ```

## Usage

```sh
$ dlorg
```

### Custom Downloads Folder

If your downloads folder is different from the default (`~/Downloads`), update the `folder` variable in `dlorg.py` to the desired path.

### Custom category configuration

If you want to manually edit the file category. You can edit the `config.json` file, whose location can be obtained by the command:
```
$ dlorg --config
```

## Folder Categories

The script sorts files into the following categories by default:

- **Audio**: 8svx, aac, ac3, aiff, amb, au, avr, caf, cdda, cvs, cvsd, cvu, dts, dvms, fap, flac, fssd, gsrt, hcom, htk, ima, ircam, m4a, m4r, maud, mp2, mp3, nist, oga, ogg, opus, paf, prc, pvf, ra, sd2, sln, smp, snd, sndr, sndt, sou, sph, spx, tta, txw, vms, voc, vox, w64, wma, wv
- **Archive**: 7z, deb, pkg, rar, rpm, tar.gz, z, zip, tar.bz2, tar.xz, gz, bz2, xz
- **Code**: c, class, cpp, cs, css, go, h, htaccess, html, java, js, json, kml, php, pl, py, rb, sql, swift, vb, yaml
- **Documents**: csv, djvu, doc, docx, odp, ods, odt, ott, pdf, ppt, rtf, txt, xls, xlsx, md
- **Ebooks**: azw3, epub, fb2, lrf, mobi, pdb, snb
- **Images**: bmp, cr2, cur, dds, dng, erf, exr, fts, gif, hdr, heic, heif, ico, jfif, jp2, jpe, jpeg, jpg, jps, mng, nef, nrw, orf, pam, pbm, pcd, pcx, pef, pes, pfm, pgm, picon, pict, png, pnm, ppm, psd, raf, ras, rw2, sfw, sgi, svg, tga, tiff, wbmp, webp, wpg, x3f, xbm, xcf, xpm, xwd
- **Programs**: apk, bin, jar, msi, exe, appimage, run, sh, fish
- **Videos**: 3gp, asf, avi, f4v, flv, hevc, m2ts, m2v, m4v, mjpeg, mkv, mov, mp4, mpeg, mpg, mts, mxf, ogv, rm, swf, ts, vob, webm, wmv
- **Fonts**: cff, dfont, otf, pfb, ps, sfd, ttf, woff

> [!NOTE]
> If no category is detected, the script will try relying on MIMEtypes. If it still returns nothing, the file will NOT be moved.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.
