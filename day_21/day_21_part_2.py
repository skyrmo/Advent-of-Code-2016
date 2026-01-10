import collections
import os
import re
from itertools import permutations


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def check(letters, input_data):
    for line in input_data:
        if line.startswith("swap position"):
            matches = re.match(r"swap position (\d+) with position (\d+)", line)
            if matches:
                pos1, pos2 = int(matches.group(1)), int(matches.group(2))
                # print(line)
                letters[pos1], letters[pos2] = letters[pos2], letters[pos1]
                # print(letters)

        elif line.startswith("swap letter"):
            matches = re.match(r"swap letter (\w+) with letter (\w+)", line)
            if matches:
                swap, swap_with = matches.group(1), matches.group(2)
                # print(line)
                for i, char in enumerate(letters):
                    if char == swap:
                        letters[i] = swap_with
                    elif char == swap_with:
                        letters[i] = swap
            # print(letters)

        elif line.startswith("move position"):
            matches = re.match(r"move position (\d+) to position (\d+)", line)
            if matches:
                from_pos, to_pos = int(matches.group(1)), int(matches.group(2))
                # print(line)
                letters.insert(to_pos, letters.pop(from_pos))
            # print(letters)

        elif line.startswith("reverse positions"):
            # print(letters)
            matches = re.match(r"reverse positions (\d+) through (\d+)", line)
            if matches:
                start, end = int(matches.group(1)), int(matches.group(2))
                # print(line)
                letters = (
                    letters[:start]
                    + letters[start : end + 1][::-1]
                    + letters[end + 1 :]
                )
            # print(letters)

        elif line.startswith("rotate based on"):
            # print(letters)
            matches = re.match(r"rotate based on position of letter (\w+)", line)
            if matches:
                match_char = matches.group(1)
                match_idxs = [i for i, k in enumerate(letters) if k == match_char]
                for idx in match_idxs:
                    moves = 1 + idx + (1 if idx >= 4 else 0)
                    for _ in range(moves):
                        letters.insert(0, letters.pop())
            # print(letters)

        elif line.startswith("rotate"):
            matches = re.match(r"rotate (\w+) (\d+) step", line)
            if matches:
                dir, rotate = matches.group(1), int(matches.group(2))
                # print(line, dir, rotate)
                if dir == "left":
                    for _ in range(rotate):
                        letters.append(letters.pop(0))
                else:
                    for _ in range(rotate):
                        letters.insert(0, letters.pop())
            # print(letters)

    return "".join(letters)


def solve(input_data):
    letters = list("abcdefgh")
    perms = permutations(letters)

    for perm in perms:
        if check(list(perm), input_data) == "fbgdceah":
            return "".join(perm)


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 21, Part Two: {result}")


if __name__ == "__main__":
    main()
