import os
import re

# import collections


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
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    i = 0

    while 0 <= i < len(input_data):
        line = input_data[i]
        if line[:3] == "cpy":
            matches = re.match(r"cpy (\w+) (\w+)", line)
            if matches:
                source, dest = matches.groups()
                if source.isdigit():
                    registers[dest] = int(source)
                else:
                    registers[dest] = registers.get(source, 0)

        elif line[:3] == "jnz":
            matches = re.match(r"jnz (\w+) (-?\d+)", line)
            if matches:
                check, dist = matches.groups()

                if check.isdigit() and int(check) != 0:
                    i += int(dist)
                    continue
                elif registers[check] != 0:
                    i += int(dist)
                    continue

        elif line[:3] == "inc":
            matches = re.match(r"inc (\w+)", line)
            if matches:
                reg = matches.group(1)
                # print(reg)
                registers[reg] += 1

        elif line[:3] == "dec":
            matches = re.match(r"dec (\w+)", line)
            if matches:
                reg = matches.group(1)
                # print(reg)
                registers[reg] -= 1

        else:
            raise ValueError(f"Invalid instruction: {line}")

        # print(registers)
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
    print(f"Solution for Day 12, Part Two: {result}")


if __name__ == "__main__":
    main()
