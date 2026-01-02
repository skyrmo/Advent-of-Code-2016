import os
import re
from collections import deque


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


class Bot:
    def __init__(self, id):
        self.id = id

        self.lo_val = None
        self.hi_val = None

        self.lo_bot = None
        self.hi_bot = None

        self.lo_out = None
        self.hi_out = None

        self.values = []

        self.ready = False

    def add_value(self, val):
        self.values.append(val)
        self.hi_val = max(self.values)

        if len(self.values) > 1:
            self.lo_val = min(self.values)

    def __repr__(self):
        return f"Bot{self.id}({self.lo_val}, {self.hi_val} | {self.lo_bot}, {self.hi_bot}, | {self.lo_out}, {self.hi_out})"


def solve(input_data):
    bots = {}
    outputs = {}

    for line in input_data:
        if line.startswith("bot"):
            arr = line.split(" ")

            bot_id = int(arr[1])

            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)

            lo_out_type, lo_out = arr[5], int(arr[6])
            hi_out_type, hi_out = arr[10], int(arr[11])

            if lo_out_type == "bot":
                bots[bot_id].lo_bot = lo_out

            if hi_out_type == "bot":
                bots[bot_id].hi_bot = hi_out

            if lo_out_type == "output":
                bots[bot_id].lo_out = lo_out

            if hi_out_type == "output":
                bots[bot_id].hi_out = hi_out

    for line in input_data:
        if line.startswith("value"):
            match = re.match(r"value (\d+) goes to bot (\d+)", line)
            if match:
                value, bot_id = int(match.group(1)), int(match.group(2))
                bots[bot_id].add_value(value)

    q: deque[Bot] = deque(
        [
            bot
            for bot in bots.values()
            if bot.lo_val is not None and bot.hi_val is not None
        ]
    )

    while q:
        bot: Bot = q.popleft()

        # if bot.lo_val == 17 and bot.hi_val == 61:
        #     return bot.id

        if bot.lo_bot is not None:
            bots[bot.lo_bot].add_value(bot.lo_val)
            if (
                bots[bot.lo_bot].lo_val is not None
                and bots[bot.lo_bot].hi_val is not None
            ):
                q.append(bots[bot.lo_bot])

        if bot.hi_bot is not None:
            bots[bot.hi_bot].add_value(bot.hi_val)
            if (
                bots[bot.hi_bot].lo_val is not None
                and bots[bot.hi_bot].hi_val is not None
            ):
                q.append(bots[bot.hi_bot])

    for _, bot in bots.items():
        if bot.lo_out is not None and bot.lo_val is not None:
            outputs[bot.lo_out] = bot.lo_val

        if bot.hi_out is not None and bot.hi_val is not None:
            outputs[bot.hi_out] = bot.hi_val

    return outputs[0] * outputs[1] * outputs[2]


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
    print(f"Solution for Day 10, Part Two: {result}")


if __name__ == "__main__":
    main()
