# import collections
import os


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
    ranges = []
    for line in input_data:
        start, end = map(int, line.split("-"))
        start = max(0, start)
        end = min(4294967295, end)
        if start <= end:
            ranges.append((start, end))

    ranges.sort()

    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    result = 0
    prev_end = 0

    for s, e in merged:
        if s > prev_end:
            result += s - prev_end
        prev_end = max(prev_end, e + 1)

    if prev_end <= 4294967295:
        result += 4294967295 - prev_end + 1

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
    print(f"Solution for Day 20, Part Two: {result}")


if __name__ == "__main__":
    main()
