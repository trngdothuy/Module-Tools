import sys
import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="Reading the file and print the content",
)

parser.add_argument("-n", action="store_true", help="Number all lines")
parser.add_argument("-b", action="store_true", help="Number only lines with content")
parser.add_argument("paths", nargs="+", help="The file path to process")

args = parser.parse_args()
paths = args.paths

for path in paths:
    try:
        with open(path, "r") as f:
            content = f.read()
        lines = content.splitlines()
        
        line_num = 1
        
        for i in range(len(lines)):
            line = lines[i]

            if args.b:
                if line != "":
                    print(f"{line_num} {line}")
                    line_num += 1
            elif args.n:
                print(f"{line_num} {line}")
                line_num += 1
            else:
                print(line)

    except Exception as e:
        print(f"Error reading {path}: {e}")