#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2023/day/3
"""


from typing import Any
from functools import reduce
from icecream import ic


def parse_schematic(lines: list[str]) -> tuple[list[Any], list[Any]]:
    numbers: list = []
    symbols: list = []
    i = 0
    for line in lines:
        numbers.append([])
        symbols.append([])

        # detect symbols
        for j in range(len(line)):
            if line[j] != "." and not line[j].isnumeric():
                symbols[i].append([line[j], (i, j), (i, j)])

        # detect substrings as numbers
        start = 0
        while start <= len(line):
            cur = start
            while (line[cur : cur + 1]).isnumeric():
                cur += 1
            if num := line[start:cur]:
                numbers[i].append([int(num), (i, start), (i, cur)])
            start = cur + 1

        i += 1
    return numbers, symbols


def is_geared(i: int, j: int, symbols: list, item: list):
    for sym in symbols[i]:
        char = sym[0]
        start = sym[1]
        end = sym[2]
        if char == "*":
            if i >= start[0] and i <= end[0]:
                if j >= start[1] and j <= end[1]:
                    # Hack, add reference to the part linked to this gear
                    # We'll come by later to count those symbols with 2 (or more) links
                    sym.append(item)
                    return True
    return False


def detect_connected_parts(numbers: list, symbols: list, lines: list):
    res = []
    for row in numbers:
        for item in row:
            num, start, end = item
            line = lines[start[0]]

            rows_to_scan: list = sorted(
                set(
                    [
                        start[0] - 1 if start[0] - 1 > 0 else 0,
                        start[0],
                        start[0] + 1 if start[0] + 1 < len(lines) else start[0],
                    ]
                )
            )

            cols_to_scan: list = sorted(
                set(
                    [
                        start[1] - 1 if start[1] - 1 > 0 else 0,
                        start[1],
                        end[1] + 1 if end[1] + 1 <= len(line) else end[1],
                    ]
                )
            )
            cols_to_scan = [cols_to_scan[0], cols_to_scan[-1]]

            for i in rows_to_scan:
                for j in range(*cols_to_scan):
                    is_geared(i, j, symbols, item)

    for row in symbols:
        for sym in row:
            if sym[0] == "*" and len(sym) > 4:
                res.append(sym[3][0] * sym[4][0])
    return res


def main() -> None:
    with open("input.txt", "rt") as f:
        lines = [f.rstrip() for f in f.readlines()]

    numbers, symbols = parse_schematic(lines)
    candidates = detect_connected_parts(numbers, symbols, lines)

    sum = reduce(lambda a, b: a + b, candidates)
    print(sum)


if __name__ == "__main__":
    main()
