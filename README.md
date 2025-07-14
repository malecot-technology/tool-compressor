# Compressor

**Compressor** is a command-line tool for losslessly optimizing common image formats including JPEG,
PNG, and SVG. It uses best-in-class utilities (`jpegtran`, `optipng`, and `svgo`) under the hood to
reduce file sizes without sacrificing quality.

Perfect for frontend developers, designers, or anyone looking to speed up web performance by
compressing images safely.

## Features

- Losslessly compresses `.jpg`, `.png`, and `.svg` files.
- Automatically chooses the right optimization method for each format.
- Only replaces files if the optimized version is smaller.
- Simple command-line interface.

## Requirements

- Python 3.7+
- `jpegtran`
- `optipng`
- `svgo`

## Usage

```bash
./compressor.py <image1> <image2> ... <imageN>
```

## Supported formats

| Format                                          | Tool       |
|-------------------------------------------------|------------|
| `.jpg`, `.jpeg`                                 | `jpegtran` |
| `.png`, `.bmp`, `.gif`, `.pnm`, `.tif`, `.tiff` | `optipng`  |
| `.svg`                                          | `svgo`     |

## Notes

- Files are only replaced if the optimized version is smaller.
- Unsupported file formats will result in an error.
- This tool is format-aware, you can safely batch multiple image types at once.

## License

This project is licensed under either of:

* [Apache License, Version 2.0](LICENSE-APACHE)
* [MIT license](LICENSE-MIT)
