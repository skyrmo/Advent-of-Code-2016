# import collections
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
    a = list("10111011111001111")
    while len(a) < 272:
        a = a + ["0"] + ["1" if x == "0" else "0" for x in a[::-1]]

    data = a[:272]
    while len(data) % 2 == 0:
        checksum = ""
        for i in range(0, len(data), 2):
            if data[i] == data[i + 1]:
                checksum += "1"
            else:
                checksum += "0"
        data = checksum

    return data


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
    print(f"Solution for Day 16, Part One: {result}")


if __name__ == "__main__":
    main()
