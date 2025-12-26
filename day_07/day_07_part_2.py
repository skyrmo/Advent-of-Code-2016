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


def check_bab(s):
    n = len(s)

    babs = []

    for i in range(n - 2):
        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            babs.append(s[i : i + 3])

    return babs


def check_aba(bab, outside_matches):
    aba = bab[1] + bab[0] + bab[1]

    for outside_match in outside_matches:
        if aba in outside_match:
            print(bab, aba, outside_match)
            return True

    return False


def solve(input_data):
    result = 0
    for line in input_data:
        print(line)
        inside_matches = re.findall(r"\[([^\]]+)\]", line)
        outside_matches = re.findall(r"[^\[\]]+(?![^\[]*\])", line)

        found_match = False
        for inside_match in inside_matches:
            babs = check_bab(inside_match)

            for bab in babs:
                # print(bab)
                if check_aba(bab, outside_matches):
                    found_match = True
                    result += 1
                    break

            if found_match:
                break

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
    print(f"Solution for Day 07, Part Two: {result}")


if __name__ == "__main__":
    main()
