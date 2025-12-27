import os
import re


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def decompress(input):
    if not input:
        return 0

    # is there a marker starting fro this position?
    marker = re.match(r"^\((\d+)x(\d+)\)", input)
    if marker:
        # extract the length and the times as int
        length, times = map(int, marker.groups())
        # note the start of the mark and the end of the expression
        start, end = marker.end(), marker.end() + length
        # return the len of the inserted string plus the len of the remainder
        return times * decompress(input[start:end]) + decompress(input[end:])

    # if not a marker
    return 1 + decompress(input[1:])


def solve(input):
    return decompress(input)


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
    print(f"Solution for Day 09, Part Two: {result}")


if __name__ == "__main__":
    main()
