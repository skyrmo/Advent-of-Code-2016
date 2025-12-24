import os
from collections import Counter


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


def solve(input_data):
    result = 0
    for line in input_data:
        checksum = line[-6:-1]
        text = line[:-11]
        sector_id = int(line[-10:-7])

        key = [
            x[0]
            for x in sorted(
                Counter([c for c in text if c != "-"]).items(),
                key=lambda x: (-x[1], x[0]),
            )
        ]

        if "".join(key[:5]) == checksum:
            result += sector_id

    return result


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
    print(f"Solution for Day 04, Part One: {result}")


if __name__ == "__main__":
    main()
