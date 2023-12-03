#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2023/day/1
"""

spelled = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}


def extract_numbers(line: str) -> tuple[str, str]:
    res = []
    line = line.rstrip()
    for i in range(len(line)):
        if line[i].isnumeric():
            res.append(line[i])
            continue
        for number in spelled.keys():
            if line.find(number, i, i + len(number)) != -1:
                res.append(spelled[number])
    print(f'{line} has {res}')
    return res[0], res[-1]


def main() -> None:
    with open("input.txt", "rt") as f:
        content = f.readlines()

    sum = 0
    for line in content:
        i, j = extract_numbers(line)
        sum += int(i + j)
        print(f"Rolling with {line.rstrip()} => {i}{j} => {sum}")
        print()

    print(sum)


if __name__ == "__main__":
    main()
