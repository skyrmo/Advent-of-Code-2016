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


def solve(input_data):
    num = 1362
    tgt = (39, 31)
    h, w = 40, 32

    grid = [["."] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            grid[r][c] = (
                "."
                if sum(
                    [
                        int(x)
                        for x in bin(
                            (c * c) + (3 * c) + (2 * c * r) + r + (r * r) + num
                        )[2:]
                    ]
                )
                % 2
                == 0
                else "#"
            )

    for row in grid:
        print(row)
    print("\n")

    q = collections.deque([(1, 1, 0)])
    grid[1][1] = 0

    while q:
        r, c, steps = q.popleft()

        for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == ".":
                q.append((nr, nc, steps + 1))
                grid[nr][nc] = steps + 1

    for row in grid:
        print(row)

    result = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] not in [".", "#"] and grid[r][c] <= 50:
                result += 1

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
    print(f"Solution for Day 13, Part Two: {result}")


if __name__ == "__main__":
    main()
