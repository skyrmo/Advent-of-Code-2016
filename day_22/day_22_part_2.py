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
        self.c = int(x)
        self.r = int(y)
        self.size = int(size)
        self.used = int(used)
        self.avail = int(avail)
        self.perc = int(perc)

    def __repr__(self):
        return f"N({self.r}, {self.c})"

    def draw(self, grid):
        def rules(node):
            if node.perc == 0:
                return "-"
            elif node.size > 100:
                return "#"
            elif node.r == 0 and node.c == 0:
                return "O"
            elif node.r == 0 and node.c == 33:
                return "G"
            else:
                return "."

        for row in grid:
            print([rules(n) for n in row])


# solved with help from https://github.com/maneatingape/advent-of-code-rust/blob/main/src/year2016/day22.rs
#
def solve(input_data):
    all_nodes = []
    for line in input_data:
        node, size, used, avail, perc = re.split(r" +", line.strip())
        node = node[15:].split("-")
        node = Node(
            node[0][1:], node[1][1:], size[:-1], used[:-1], avail[:-1], perc[:-1]
        )
        all_nodes.append(node)

    w, h = 34, 31
    empty = None
    wall_c = w

    grid = [[None] * w for _ in range(h)]

    for node in all_nodes:
        grid[node.r][node.c] = node
        if node.perc == 0:
            empty = node

        if node.size > 100:
            wall_c = min(wall_c, node.c - 1)

    left = empty.c - wall_c
    up = empty.r
    right = (w - 2) - wall_c
    data = 1
    empty = (w - 2) * 5

    return left + up + right + data + empty


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
    print(f"Solution for Day 22, Part Two: {result}")


if __name__ == "__main__":
    main()
