import os


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
    h, w = 6, 50

    grid = [[0] * w for _ in range(h)]

    for line in input_data:
        if line.startswith("rect"):
            _, size = line.split()
            rec_w, rec_h = [int(x) for x in size.split("x")]
            # print(line, rec_w, rec_h)

            for r in range(int(rec_h)):
                for c in range(int(rec_w)):
                    grid[r][c] = 1

        elif line.startswith("rotate row"):
            _, _, row, _, shift = line.split(" ")
            row = int(row[2:])
            shift = int(shift)
            grid[row] = grid[row][-shift:] + grid[row][:-shift]

        elif line.startswith("rotate column"):
            _, _, col, _, shift = line.split()
            col = int(col[2:])
            shift = int(shift)
            old_row = [grid[r][col] for r in range(h)]
            new_row = old_row[-shift:] + old_row[:-shift]
            for r in range(h):
                grid[r][col] = new_row[r]

    result = 0
    for row in grid:
        result += sum(row)

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
    print(f"Solution for Day 08, Part One: {result}")


if __name__ == "__main__":
    main()
