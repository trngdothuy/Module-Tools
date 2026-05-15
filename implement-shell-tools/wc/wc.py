import sys
import argparse
import os

parser = argparse.ArgumentParser(
    prog="wc",
    description="Word count",
)

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
parser.add_argument("paths", nargs="+", help="The files to process")

args = parser.parse_args()

totalLines = 0
totalWords = 0
totalBytes = 0

for path in args.paths:
    try:
        with open(path, "rb") as f:
            buffer = f.read()
        content = buffer.decode("utf-8") #, errors="ignore"
            
        lines = len(content.split("\n")) - 1
        wordCount = len(content.strip().split())
        byte_count = len(buffer)
        
        totalLines += lines
        totalWords += wordCount
        totalBytes += byte_count
        
        if args.l:
            print(f"{lines}      {path}")
        elif args.w:
            print(f"{wordCount}      {path}")
        elif args.c:
            print(f"{bytes}      {path}")
        else:
            print(f"{lines}      {wordCount}       {bytes}      {path}")
    except Exception as e:
        print(f"Error reading {path}: {e}")
        
if len(args.paths) > 1:
    if args.l:
        print(f"{totalLines}      total")
    elif args.w:
        print(f"{totalWords}      total")
    elif args.c:
        print(f"{totalBytes}      total")
    else:
        print(f"{totalLines}      {totalWords}      {totalBytes}      total")
