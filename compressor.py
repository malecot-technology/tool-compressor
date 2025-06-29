#!/usr/bin/env python3
import subprocess
import argparse
from pathlib import Path


def optimize_jpeg(filepath):
    temp_file = Path(filepath).with_suffix(".opt.jpg")
    cmd = [
        "jpegtran",
        "-copy",
        "none",
        "-optimize",
        "-perfect",
        "-progressive",
        "-outfile",
        str(temp_file),
        str(filepath),
    ]
    subprocess.run(cmd, check=True)
    if temp_file.stat().st_size < Path(filepath).stat().st_size:
        temp_file.replace(filepath)
    else:
        temp_file.unlink()
        print(f"{filepath} is already optimized.")


def optimize_png(filepath):
    orig_size = Path(filepath).stat().st_size
    subprocess.run(["optipng", "-o7", str(filepath)], check=True)
    new_size = Path(filepath).stat().st_size


def optimize_svg(filepath):
    orig_size = Path(filepath).stat().st_size
    subprocess.run(["svgo", "--multipass", str(filepath)], check=True)
    new_size = Path(filepath).stat().st_size


def main():
    parser = argparse.ArgumentParser(description="Losslessly optimize images.")
    parser.add_argument("files", nargs="+", help="List of images to optimize")
    args = parser.parse_args()
    for filepath in args.files:
        ext = Path(filepath).suffix.lower()
        if ext in [".jpg", ".jpeg"]:
            optimize_jpeg(filepath)
        elif ext in [".png", ".bmp", ".gif", ".pnm", ".tif", ".tiff"]:
            optimize_png(filepath)
        elif ext == ".svg":
            optimize_svg(filepath)
        else:
            parser.error(f"Unsupported file type: {ext}.")


if __name__ == "__main__":
    main()
