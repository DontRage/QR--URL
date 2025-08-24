#!/usr/bin/env python3
import sys
import subprocess
import re
from pyzbar.pyzbar import decode
from PIL import Image

def pick_image_file():
    try:
        result = subprocess.run(
            ["zenity", "--file-selection", "--title=Select an image with a QR code",
             "--file-filter=Images | *.png *.jpg *.jpeg *.bmp *.gif *.tif *.tiff"],
            capture_output=True,
            text=True,
            check=True
        )
        path = result.stdout.strip()
        return path if path else None
    except:
        return None

def is_url(s):
    return bool(re.match(r'^(https?://|www\.)', s, re.IGNORECASE))

def decode_qr_from_image(path):
    with Image.open(path) as img:
        decoded_objects = decode(img)
    return [obj.data.decode("utf-8", errors="replace") for obj in decoded_objects]

def main():
    img_path = sys.argv[1] if len(sys.argv) > 1 else None
    if not img_path:
        img_path = pick_image_file()
        if not img_path:
            print("No image provided or selected.")
            sys.exit(2)

    decoded = decode_qr_from_image(img_path)
    if not decoded:
        print("No QR codes found in the image.")
        sys.exit(3)

    urls = [s for s in decoded if is_url(s)]
    if urls:
        for u in urls:
            print("URL:", u)
    else:
        for s in decoded:
            print("QR data:", s)

if __name__ == "__main__":
    main()

