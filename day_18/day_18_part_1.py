import collections
import os


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


def solve(input_data):
    w = len(input_data)
    tiles = [input_data]
    result = sum([1 if x == "." else 0 for x in input_data])

    for _ in range(39):
        prev = tiles[-1]
        next_row = ""

        for i in range(w):
            prev_slice = prev[max(i - 1, 0) : min(i + 2, w)]
            if i == 0 and prev_slice in ["^^", ".^"]:
                next_row += "^"
            elif i == w - 1 and prev_slice in ["^^", "^."]:
                next_row += "^"
            elif prev_slice in ["^^.", ".^^", "^..", "..^"]:
                next_row += "^"
            else:
                next_row += "."

        result += sum([1 if x == "." else 0 for x in next_row])

        tiles.append(next_row)

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
    print(f"Solution for Day 18, Part One: {result}")


if __name__ == "__main__":
    main()
