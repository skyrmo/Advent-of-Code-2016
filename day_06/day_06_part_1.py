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
    counters = [[0] * 26 for _ in range(len(input_data[0]))]

    for line in input_data:
        for i, char in enumerate(line):
            c_idx = ord(char) - ord("a")
            counters[i][c_idx] += 1

    result = ""
    for counter in counters:
        max_idx = 0
        for i in range(26):
            if counter[i] > counter[max_idx]:
                max_idx = i
        result += chr(max_idx + ord("a"))

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
    print(f"Solution for Day 06, Part One: {result}")


if __name__ == "__main__":
    main()
