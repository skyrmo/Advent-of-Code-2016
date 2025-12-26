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


def check_pattern(s):
    n = len(s)

    for i in range(n - 3):
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            return True

    return False


def solve(input_data):
    result = 0
    for line in input_data:
        inside_matches = re.findall(r"\[([^\]]+)\]", line)
        outside_matches = re.findall(r"[^\[\]]+(?![^\[]*\])", line)

        # Look for a reason to "disqualify" this line
        for inside_match in inside_matches:
            if check_pattern(inside_match):
                break  # We found an ABBA inside; stop looking at these brackets
        else:
            # This block runs ONLY if the 'inside' loop finished WITHOUT breaking.
            # It means NO check_pattern was True inside the brackets.
            for outside_match in outside_matches:
                if check_pattern(outside_match):
                    print("Found outside match:", outside_match)
                    result += 1
                    break  # Assuming one match per line is enough

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
    print(f"Solution for Day 07, Part One: {result}")


if __name__ == "__main__":
    main()
