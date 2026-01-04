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


# 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6
# 1 2 3 4 5 6 7 8 9101112 0 1 2 3 4 5 6 7 8 9 10 11 12 0
#
# Disc #1 has 7 positions; at time=0, it is at position 0.
# Disc #2 has 13 positions; at time=0, it is at position 0.
# Disc #3 has 3 positions; at time=0, it is at position 2.
# Disc #4 has 5 positions; at time=0, it is at position 2.
# Disc #5 has 17 positions; at time=0, it is at position 0.
# Disc #6 has 19 positions; at time=0, it is at position 7.

input_data = [
    (1, 7, 0),
    (2, 13, 0),
    (3, 3, 2),
    (4, 5, 2),
    (5, 17, 0),
    (6, 19, 7),
]

# input_data = [
#     (1, 5, 4),
#     (2, 2, 1),
# ]


class Disk:
    def __init__(self, id, positions, start):
        self.id = id
        self.positions = positions
        self.start = start
        self.position = start

    def turn(self):
        self.position = (self.position + 1) % self.positions

    @property
    def is_aligned(self):
        return (self.position + self.id) % self.positions == 0

    def __repr__(self):
        return f"Disk({self.id}, {self.positions}, {self.position})"


def solve(d):
    disks = [Disk(id, positions, start) for id, positions, start in input_data]

    time = 0
    while True:
        for disk in disks:
            disk.turn()

        if all([d.is_aligned for d in disks]):
            return time

        time += 1


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
    print(f"Solution for Day 15, Part One: {result}")


if __name__ == "__main__":
    main()
