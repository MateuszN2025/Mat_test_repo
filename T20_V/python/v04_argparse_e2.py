import argparse

parser = argparse.ArgumentParser(description="MatApp")
parser.add_argument("--name", default="MatApp")
parser.add_argument("--num", default=100)
args = parser.parse_args()
print(f"Hello {args.name} {args.num}")