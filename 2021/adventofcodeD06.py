import sys
from functools import lru_cache

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    fishies = [(int(item)) for item in input_file.readline().strip().replace('\n', '').split(',')]
    input_file.close()
    return fishies


@lru_cache(256)
def fish_pop(days, d=0, t=8):
    fish_count = 0
    for i in range(d, days):
        if t == 0:
            t = 7
            fish_count += 1 + fish_pop(days, i + 1)
        t -= 1
    return fish_count


def part1(fishies):
    fish_count = len(fishies)
    for fish in fishies:
        fish_count += fish_pop(80, 0, fish)
    return fish_count


def part2(fishies):
    fish_count = len(fishies)
    for fish in fishies:
        fish_count += fish_pop(256, 0, fish)
    return fish_count


def main():
    fishies = load_data(file_name)
    # Part1
    print(part1(fishies))
    # Part2
    print(part2(fishies))


if __name__ == '__main__':
    main()
