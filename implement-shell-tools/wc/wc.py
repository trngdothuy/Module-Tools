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

total_lines = 0
total_words = 0
total_bytes = 0

for path in args.paths:
    try:
        with open(path, "rb") as f:
            buffer = f.read()
        content = buffer.decode("utf-8") #, errors="ignore"
            
        lines = len(content.split("\n")) - 1
        word_count = len(content.strip().split())
        byte_count = len(buffer)
        
        total_lines += lines
        total_words += word_count
        total_bytes += byte_count
            
        if args.c and args.l:
            print(f"{lines}      {byte_count}      {path}")
        elif args.c and args.w:
            print(f"{word_count}      {byte_count}      {path}")
        elif args.l and args.w:
            print(f"{lines}      {word_count}      {path}")
        elif args.l:
            print(f"{lines}      {path}")
        elif args.w:
            print(f"{word_count}      {path}")
        elif args.c:
            print(f"{byte_count}      {path}")
        else:
            print(f"{lines}      {word_count}       {byte_count}      {path}")
    except Exception as e:
        print(f"Error reading {path}: {e}")
        
if len(args.paths) > 1:
    if args.l:
        print(f"{total_lines}      total")
    elif args.w:
        print(f"{total_words}      total")
    elif args.c:
        print(f"{total_bytes}      total")
    else:
        print(f"{total_lines}      {total_words}      {total_bytes}      total")
