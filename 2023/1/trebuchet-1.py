#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2023/day/1
"""

def extract_numbers(line: str) -> tuple[str, str]:
    res = [str(c) for c in line if c.isnumeric()]
    return res[0], res[-1]

def main() -> None:
    with open('input.txt', 'rt') as f:
        content = f.readlines()

    sum = 0
    for line in content:
        i, j = extract_numbers(line)
        sum += int(i + j)
        print(f'Rolling with {line.rstrip()} => {i}{j} => {sum}')

    print(sum)

if __name__ == '__main__':
    main()
