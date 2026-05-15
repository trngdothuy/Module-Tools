import sys
import argparse
import os

parser = argparse.ArgumentParser(
    prog="ls",
    description="List all files name",
)

parser.add_argument("-1", dest="one", action="store_true", help="A new line for each file")
parser.add_argument("-a", action="store_true", help="Show hidden files")
parser.add_argument("path", nargs="?", default=".", help="The directory to list")

args = parser.parse_args()
path = args.path

try:
    files = sorted(os.listdir(path))
    if not args.a:
        files = [file for file in files if not file.startswith(".")]
    if args.one:
        print("\n".join(files))
    else:
        print("       ".join(files))

except Exception as e:
    print(f"Error reading {path}: {e}")