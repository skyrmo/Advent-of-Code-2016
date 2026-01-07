import collections
import os
from hashlib import md5


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
    h, w = 4, 4
    hash = "ioramepc"
    q = collections.deque([(0, 0, "")])
    result = 0

    while q:
        r, c, path = q.popleft()

        if r == h - 1 and c == w - 1:
            result = max(result, len(path))
            continue

        hash_input = hash + path
        dir_hash = md5(hash_input.encode()).hexdigest()[:4]

        for idx, nr, nc in ((0, r - 1, c), (1, r + 1, c), (2, r, c - 1), (3, r, c + 1)):
            if 0 <= nr < h and 0 <= nc < w and dir_hash[idx] in "bcdef":
                q.append((nr, nc, path + "UDLR"[idx]))

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    # input_path = os.path.join(script_dir, 'input.txt')
    input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 17, Part Two: {result}")


if __name__ == "__main__":
    main()
