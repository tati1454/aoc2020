import os
import sys
import argparse

import requests

try:
    token = os.environ["AOC_TOKEN"]
except KeyError:
    print("Create AOC_TOKEN env")
    exit(1)

try:
    day = sys.argv[1]
except IndexError:
    print("Usage: getInput.py <day>")
    exit(1)

r = requests.get(f"https://adventofcode.com/2020/day/{day}/input", cookies={"session": token})

with open("input.txt", "w") as f:
    f.write(r.text)