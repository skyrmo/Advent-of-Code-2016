import hashlib
import os
from collections import deque

# import collections


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


def stretch_hash(h):
    for _ in range(2016):
        new_hash = hashlib.md5(h.encode()).hexdigest()
        h = new_hash
    return h


def solve(input_data):
    next_1000 = deque()
    for i in range(1, 1002):
        input = input_data + str(i)
        md5 = hashlib.md5(input.encode()).hexdigest()
        next_1000.append(stretch_hash(md5))

    results_found = 0
    i = 1
    while True:
        md5 = next_1000.popleft()

        for j in range(30):  # 30 magic number = 32 bit hash length - 2
            if md5[j] == md5[j + 1] == md5[j + 2]:
                for next_hash in next_1000:
                    if md5[j] * 5 in next_hash:
                        results_found += 1
                        if results_found == 64:
                            return i

                        break
                break

        next_input = input_data + str(i + 1001)
        next_md5 = hashlib.md5(next_input.encode()).hexdigest()
        next_1000.append(stretch_hash(next_md5))

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
    print(f"Solution for Day 14, Part Two: {result}")


if __name__ == "__main__":
    main()
