#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2023/day/2
"""

import re
from collections import defaultdict
import json
from functools import reduce

# Limits
bag = {"red": 12, "green": 13, "blue": 14}


def main() -> None:
    with open("input.txt", "rt") as f:
        content = [f.rstrip() for f in f.readlines()]

    tally = 0

    for line in content:
        game_id, data = re.split(": ", line)
        game_id = re.search("([0-9]+)", game_id).group(0)

        round_tally = defaultdict(list)
        for round in re.split("; ", data):
            for item in re.split(", ?", round):
                count, colour = re.split(" +", item)
                count = int(count)
                round_tally[colour].append(count)

        power_set = []
        for colour, counts in round_tally.items():
            power_set.append(max(round_tally[colour]))

        power = reduce(lambda a, b: a * b, power_set)
        tally += power

    print(f"tally: {tally}")


if __name__ == "__main__":
    main()
