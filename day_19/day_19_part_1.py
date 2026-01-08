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


class Node:
    def __init__(self, id, val, next=None):
        self.id = id
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.id}, {self.val})"


def solve(input_data):
    dummy_head = Node(-1, -1)
    prev = dummy_head

    for i in range(1, 3014388):
        node = Node(i, 1)
        prev.next = node
        prev = node

    prev.next = dummy_head.next

    cur = dummy_head.next

    while cur.next:
        if cur.next.id == cur.id:
            return cur.id

        cur.val += cur.next.val
        cur.next = cur.next.next

        cur = cur.next

    # return dummy_head.next.value


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
    print(f"Solution for Day 19, Part One: {result}")


if __name__ == "__main__":
    main()
