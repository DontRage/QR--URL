# QR--URL

A small Python utility that decodes QR codes from an image and prints any URLs it finds.

## Features
- Accepts an image path as a command line argument or prompts for one via a Zenity file picker.
- Uses `pyzbar` and `Pillow` to decode QR codes.
- Prints URLs when detected, otherwise prints the raw QR data.

## Requirements
- Python 3
- [pyzbar](https://pypi.org/project/pyzbar/)
- [Pillow](https://pypi.org/project/Pillow/)
- Optional: [Zenity](https://help.gnome.org/users/zenity/stable/) for the file selection dialog

Install the Python dependencies with:

```bash
pip install pyzbar Pillow
```

## Usage
Provide an image file containing a QR code:

```bash
python scan_qr.py path/to/image.png
```

If no argument is given, the script tries to open a file chooser using Zenity. The decoded URLs or data are printed to the terminal.

