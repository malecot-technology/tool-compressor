# Compressor

**Compressor** is a command-line tool for losslessly optimizing common image formats including JPEG,
PNG, SVG, along with PDF documents. It uses best-in-class utilities (`jpegtran`, `optipng`, `svgo`,
and `ghostscript`) under the hood to reduce file sizes without sacrificing quality.

Perfect for frontend developers, designers, or anyone looking to speed up web performance by
compressing images and documents safely.

## Features

- Losslessly compresses `.jpg`, `.png`, `.svg`, and `.pdf` files.
- Automatically chooses the right optimization method for each format.
- Only replaces files if the optimized version is smaller.
- Simple command-line interface.

## Requirements

- Python 3.7+
- `jpegtran`
- `optipng`
- `svgo`
- `ghostscript`

## Usage

```bash
./compressor.py <file1> <file2> ... <fileN>
```

## Supported formats

| Format                                          | Tool          |
|-------------------------------------------------|---------------|
| `.jpg`, `.jpeg`                                 | `jpegtran`    |
| `.png`, `.bmp`, `.gif`, `.pnm`, `.tif`, `.tiff` | `optipng`     |
| `.svg`                                          | `svgo`        |
| `.pdf`                                          | `ghostscript` |

## Notes

- Files are only replaced if the optimized version is smaller.
- Unsupported file formats will result in an error.
- This tool is format-aware, you can safely batch multiple image/document types at once.

## License

This project is licensed under either of:

* [Apache License, Version 2.0](LICENSE-APACHE)
* [MIT license](LICENSE-MIT)
