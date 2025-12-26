import hashlib
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
    result = [-1] * 8
    i = 1
    changed = 0

    while True:
        hash = hashlib.md5((input_data + str(i)).encode()).hexdigest()

        if hash.startswith("00000"):
            pos = int(hash[5], 16)

            if pos < 8 and result[pos] < 0:
                changed += 1
                result[pos] = ord(hash[6])

            if changed == 8:
                return "".join([chr(x) for x in result])

        i += 1


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
    print(f"Solution for Day 05, Part Two: {result}")


if __name__ == "__main__":
    main()
