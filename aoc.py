#!/usr/bin/env python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("days", nargs="+")
args = parser.parse_args()

from pathlib import Path
from subprocess import run


def main(args):
    for day in args.days:
        file = Path(f"py/{day}.py")
        if file.exists():
            run(["python", file])


if __name__ == "__main__":
    main(args)
