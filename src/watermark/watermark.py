"""
This module provides high-level functions for embedding and extracting watermarks
from images, handling file operations and providing console feedback.
"""
from .lib._watermark_impl import _watermark_apply, _watermark_extract  # pyright: ignore[reportMissingImports]


def watermark_apply(input_image_path: str, asset_file_path: str, password: str, output_image_path: str) -> bool:
    print(f"\n--- Embedding '{asset_file_path}' in '{input_image_path}' -> '{output_image_path}' ---")

    success = False
    try:
        _watermark_apply(input_image_path, asset_file_path, password, output_image_path)
        success = True
    except FileNotFoundError as e:
        print(f"Embedding file not found {e}")
    except Exception as e:
        print(f"An unexpected error occurred during embedding: {e}")

    if success:
        print(f"SUCCESS: Watermark encrypted and embedded to: {output_image_path}")
    return success


def watermark_extract(watermarked_image_path: str, password: str, output_asset_file_path: str) -> bool:
    print(f"\n--- Extracting: {watermarked_image_path} -> {output_asset_file_path} ---")

    success = False
    try:
        _watermark_extract(watermarked_image_path, password, output_asset_file_path)
        success = True
    except FileNotFoundError as e:
        print(f"Watermarked file not found {e}")
    except Exception as e:
        print(f"An unexpected error occurred during extracting: {e}")

    if success:
        print(f"SUCCESS: Asset successfully extracted and saved to: {output_asset_file_path}")
    return success


if __name__ == "__main__":
    print("This script is intended to be run as a module, not as a standalone program.")
