import os
from collections import deque
from copy import deepcopy
from itertools import combinations
from typing import List, Set


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


class Item:
    def __init__(self, id: int, type: str):
        self.id = id
        self.type = type

    def __repr__(self) -> str:
        return f"Item({self.id} {self.type})"

    def __eq__(self, other):
        return hash((self.id, self.type)) == hash((other.id, other.type))

    def __hash__(self):
        return hash((self.id, self.type))


class Floor:
    def __init__(self, generators: set, chips: set):
        self.generators = generators
        self.chips = chips

    @property
    def items(self) -> Set[Item]:
        return self.generators.union(self.chips)

    def give(self, item):
        if item.type == "G":
            self.generators.remove(item)
        else:
            self.chips.remove(item)

    def receive(self, item):
        if item.type == "G":
            self.generators.add(item)
        else:
            self.chips.add(item)

    def __repr__(self):
        return f"Floor({self.generators}, {self.chips})"


class State:
    def __init__(self, elevator: int, floors: List[Floor], steps: int):
        self.elevator = elevator
        self.floors = floors
        self.steps = steps
        self.top_floor = len(floors)

    @property
    def bottom_floor(self) -> int:
        for i in range(self.top_floor - 1):
            if len(self.floors[i].items) > 0:
                return i
        return self.top_floor - 1

    def __repr__(self):
        return (
            f"State(elevator={self.elevator}, floors={self.floors}, steps={self.steps})"
        )

    def __hash__(self):
        floors = {}

        for i, floor in enumerate(self.floors):
            for item in floor.chips:
                floors[item.id] = [i]

        for i, floor in enumerate(self.floors):
            for item in floor.generators:
                floors[item.id].append(i)

        return hash(str(sorted(floors.values())) + str(self.elevator))

    def __eq__(self, other):
        return hash(self) == hash(other)

    @property
    def is_complete(self):
        return all(len(floor.items) == 0 for floor in self.floors[:-1])

    @property
    def is_valid(self):
        for floor in self.floors:
            if floor.generators == set():
                continue

            for chip in floor.chips:
                if not any(chip.id == gen.id for gen in floor.generators):
                    return False
        return True

    def next_states(self):
        cur_floor = self.floors[self.elevator]

        for dir in [-1, 1]:
            if (
                self.elevator + dir < self.bottom_floor
                or self.elevator + dir >= self.top_floor
            ):
                continue
            for num_items in [1, 2]:
                for items in combinations(cur_floor.items, num_items):
                    new_state = self._generate_new_state(dir, items)
                    if new_state.is_valid:
                        yield new_state

    def _generate_new_state(self, dir, items):
        new_floors = deepcopy(self.floors)
        for item in items:
            new_floors[self.elevator].give(item)
            new_floors[self.elevator + dir].receive(item)

        return State(
            elevator=self.elevator + dir, floors=new_floors, steps=self.steps + 1
        )


start_items = [
    (1, "M", 1),
    (3, "M", 1),
    (1, "G", 0),
    (2, "G", 0),
    (2, "M", 0),
    (3, "G", 0),
    (4, "G", 0),
    (4, "M", 0),
    (5, "G", 0),
    (5, "M", 0),
]


def solve(input_data):
    state = State(
        floors=[
            Floor(set(), set()),
            Floor(set(), set()),
            Floor(set(), set()),
            Floor(set(), set()),
        ],
        elevator=0,
        steps=0,
    )

    for id, type, floor in start_items:
        item = Item(id, type)
        state.floors[floor].receive(item)

    # print(state)

    queue = deque([state])
    visited = set()

    while queue:
        cur_state = queue.popleft()
        # print(cur_state)

        if cur_state.is_valid and cur_state.is_complete:
            print(cur_state.steps)
            return cur_state.steps

        if cur_state in visited:
            continue

        visited.add(cur_state)

        for next_state in cur_state.next_states():
            # print(next_state)
            if next_state.is_valid and next_state not in visited:
                queue.append(next_state)


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
    print(f"Solution for Day 11, Part One: {result}")


if __name__ == "__main__":
    main()
