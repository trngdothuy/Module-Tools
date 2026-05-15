import cowsay
import sys
import argparse

parser = argparse.ArgumentParser(
    prog="cow-say",
    description="Make animals say things",
)

parser.add_argument("--animal", help="Choose the animal to draw", default="cow")
parser.add_argument("message", help="The sentence for animals to say", nargs="+")

args = parser.parse_args()
animal = args.animal
text = args.message

try: 
    getattr(cowsay, animal)(" ".join(text))
except AttributeError:
    print(f"Unknown animal: {animal}")