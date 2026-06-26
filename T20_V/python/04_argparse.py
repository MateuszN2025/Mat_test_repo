import argparse

parser = argparse.ArgumentParser(description="Simple demo")
parser.add_argument("--name", default="World")
args = parser.parse_args()

print(f"Hello {args.name}")

# python3 ./python/04_argparse.py --help
# python3 ./python/04_argparse.py --name Mike
#   Hello Mike

# Without argparse, the same idea would look more manual.
# You read raw values from sys.argv and handle defaults yourself.

"""import sys

name = "World"
if len(sys.argv) > 1:
    name = sys.argv[1]

print(f"Hello {name}")"""

# Example run:
# python3 ./python/04_argparse.py Mike
# Hello Mike