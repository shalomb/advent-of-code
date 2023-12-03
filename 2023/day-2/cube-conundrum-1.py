#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2023/day/2
"""

import re
from collections import defaultdict

# Limits
bag = {"red": 12, "green": 13, "blue": 14}


def main() -> None:
    with open("input.txt", "rt") as f:
        content = [f.rstrip() for f in f.readlines()]

    tally = 0

    for line in content:
        game_id, data = re.split(": ", line)
        game_id = re.search("([0-9]+)", game_id).group(0)

        game_tally = defaultdict(list)
        for round in re.split("; ", data):
            round_tally = {}
            for item in re.split(", ?", round):
                count, colour = re.split(" +", item)
                round_tally[colour] = int(count)

            game_tally[game_id].append(
                all([count <= bag[colour] for colour, count in round_tally.items()])
            )

        if all(game_tally[game_id]):
            tally += int(game_id)

    print(f"tally: {tally}")


if __name__ == "__main__":
    main()
