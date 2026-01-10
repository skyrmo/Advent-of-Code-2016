import collections
import os
import re


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


class Node:
    def __init__(self, x, y, size, used, avail, perc):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.used = int(used)
        self.avail = int(avail)
        self.perc = int(perc)

    def __repr__(self):
        return f"Node(x={self.x}, y={self.y}) size={self.size}"


def solve(input_data):
    all_nodes = []
    result = 0
    for line in input_data:
        node, size, used, avail, perc = re.split(r" +", line.strip())
        node = node[15:].split("-")
        node = Node(
            node[0][1:], node[1][1:], size[:-1], used[:-1], avail[:-1], perc[:-1]
        )
        all_nodes.append(node)

    for a in all_nodes:
        for b in all_nodes:
            if a == b:
                continue

            if a.used > 0 and a.used <= b.avail:
                result += 1

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
    print(f"Solution for Day 22, Part One: {result}")


if __name__ == "__main__":
    main()
