import sys
import argparse
from pathlib import Path
from watermark.watermark import watermark_apply, watermark_extract


def main() -> int:
    script_name = Path(sys.argv[0]).name

    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="A watermarking and extraction tool for pictures.",
        epilog="Usage examples: \n"
               f"  - Embed watermark: python {script_name} embed -i input_picture -w watermark_file -p key -o watermarked.png\n"
               f"  - Extract watermark: python {script_name} extract -i watermarked.png -p key -o watermark_file",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Use a subparser to handle multiple commands (embed/extract)
    subparsers = parser.add_subparsers(dest='command', required=True, help='Action to perform')

    # 1. EMBED Subparser
    parser_embed = subparsers.add_parser('embed', help='Embed a watermark into a picture.')
    parser_embed.add_argument('-i', '--input', required=True, help='Path to the input picture file (JPEG/PNG).')
    parser_embed.add_argument('-w', '--watermark', required=True, help='Path to the file containing the watermark to embed.') 
    parser_embed.add_argument('-p', '--password', required=True, help='The password for watermark encryption.')
    parser_embed.add_argument('-o', '--output', required=True, help='Path to save the resulting watermarked picture file (PNG).')
    
    # 2. EXTRACT Subparser
    parser_extract = subparsers.add_parser('extract', help='Extract a watermark from a picture.')
    parser_extract.add_argument('-i', '--input', required=True, help='Path to the input watermarked picture file (PNG).')
    parser_extract.add_argument('-p', '--password', required=True, help='The password for watermark decryption.')
    parser_extract.add_argument('-o', '--output', required=True, help='Path to save the file containing the extracted watermark.') 

    # Parse arguments
    args = parser.parse_args()

    # Dispatch command to the relevant function
    exit_code = -1  # error
    if args.command == 'embed':
        if (watermark_apply(args.input, args.watermark, args.password, args.output)):
            exit_code = 0  # success
    elif args.command == 'extract':
        if (watermark_extract(args.input, args.password, args.output)):
            exit_code = 0  # success

    return exit_code


if __name__ == "__main__":
    exit(main())
