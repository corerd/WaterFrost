"""
Module for testing the watermarking functionality.
This script verifies that assets can be successfully embedded into a carrier image 
and subsequently extracted using a password.
"""

import sys
import os
import shutil

# Add the source scripts directory to the Python path
CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
PYTHON_SCRIPTS = os.path.join(CURRENT_DIRECTORY, "..", "src")
sys.path.insert(0, PYTHON_SCRIPTS)

from watermark.watermark import watermark_apply, watermark_extract

CARRIER_PATH = os.path.join(CURRENT_DIRECTORY, "carrier.jpg")
ASSET_PATH = os.path.join(CURRENT_DIRECTORY, "asset.txt")
OUTPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "output")
PASSWORD = "ThisIsNotASecret"


if __name__ == "__main__":
    print(f"Refresh >{OUTPUT_DIRECTORY}< directory")
    if os.path.exists(OUTPUT_DIRECTORY):
        shutil.rmtree(OUTPUT_DIRECTORY)
    os.makedirs(OUTPUT_DIRECTORY)

    asset_extension = os.path.splitext(ASSET_PATH)[1]
    ASSET_RECOVERED_PATH = os.path.join(OUTPUT_DIRECTORY, "asset_recovered"+asset_extension)
    WATERMARKED_IMAGE_PATH = os.path.join(OUTPUT_DIRECTORY, "watermarked.png")

    # Embed and extract an asset as a watermark
    watermark_apply(CARRIER_PATH, ASSET_PATH, PASSWORD, WATERMARKED_IMAGE_PATH)
    watermark_extract(WATERMARKED_IMAGE_PATH, PASSWORD, ASSET_RECOVERED_PATH)

    # Verify if the recovered asset matches the original source
    with open(ASSET_PATH, 'rb') as binary_f1:
        original_content = binary_f1.read()
    with open(ASSET_RECOVERED_PATH, 'rb') as binary_f2:
        recovered_content = binary_f2.read()

    if original_content != recovered_content:
        print("FAILED: The recovered asset does not match the original.")
        exit(-1)

    print("SUCCESS: The recovered asset is identical to the original.")
