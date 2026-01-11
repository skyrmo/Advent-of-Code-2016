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
        return [list(line) for line in data.split("\n")]

        return data


def solve(grid):
    h, w = len(grid), len(grid[0])
    result = float("inf")
    locations = set()
    mask = 0
    visited = {}
    start_pos = (-1, -1)

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "0":
                start_pos = (r, c)
            if cell not in ["#", "."]:
                locations.add(cell)

    q = collections.deque([(start_pos, 1, 0)])
    visited[(start_pos[0], start_pos[1], 1)] = 0
    end_states = []

    while q:
        (r, c), mask, steps = q.popleft()

        num_visited = bin(mask).count("1")
        if num_visited == len(locations):
            end_states.append(((r, c), steps))
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
                if grid[nr][nc] == ".":
                    if (nr, nc, mask) not in visited:
                        q.append(((nr, nc), mask, steps + 1))
                        visited[(nr, nc, mask)] = steps + 1
                else:
                    new_mask = mask | (1 << int(grid[nr][nc]))
                    q.append(((nr, nc), new_mask, steps + 1))
                    visited[(nr, nc, new_mask)] = steps + 1

    q = collections.deque()
    for pos, steps in end_states:
        q.append((pos, steps, set([pos])))

    while q:
        pos, steps, visited = q.popleft()
        r, c = pos

        if (r, c) == start_pos:
            result = min(result, steps)

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                0 <= nr < h
                and 0 <= nc < w
                and grid[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                q.append(((nr, nc), steps + 1, visited))

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
    print(f"Solution for Day 24, Part Two: {result}")


if __name__ == "__main__":
    main()
