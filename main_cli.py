import os
import sys

# Add the source scripts directory to the Python path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))), "src"))

from cli import main


if __name__ == "__main__":
    exit(main())
