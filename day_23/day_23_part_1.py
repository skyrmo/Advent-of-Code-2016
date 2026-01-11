# import collections
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


def solve(input_data):
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    instructions = [line.split() for line in input_data]
    n = len(instructions)
    i = 0

    def get_val(x):
        try:
            return int(x)
        except ValueError:
            return registers[x]

    while 0 <= i < n:
        inst = instructions[i]
        op = inst[0]

        if op == "cpy":
            if inst[2] in registers:
                registers[inst[2]] = get_val(inst[1])

        elif op == "inc":
            if inst[1] in registers:
                registers[inst[1]] += 1

        elif op == "dec":
            if inst[1] in registers:
                registers[inst[1]] -= 1

        elif op == "jnz":
            if get_val(inst[1]) != 0:
                i += get_val(inst[2])
                continue

        elif op == "tgl":
            offset = get_val(inst[1])
            tgt_idx = i + offset

            if 0 <= tgt_idx < n:
                inst = instructions[tgt_idx]
                if len(inst) == 2:
                    inst[0] = "dec" if inst[0] == "inc" else "inc"
                elif len(inst) == 3:
                    inst[0] = "cpy" if inst[0] == "jnz" else "jnz"

        i += 1

    return registers["a"]


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
    print(f"Solution for Day 23, Part One: {result}")


if __name__ == "__main__":
    main()
