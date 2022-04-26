import sys

import numpy as np

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    crabs = [(int(item)) for item in input_file.readline().strip().replace('\n', '').split(',')]
    input_file.close()
    return crabs


def part1(crabs):
    median = int(np.median(crabs))
    fuel = [0, 0]
    fuel[0] = np.sum(np.abs(np.subtract(crabs, median)))
    fuel[1] = np.sum(np.abs(np.subtract(crabs, median + 1)))
    return np.min(fuel)


def part2(crabs):
    mean = int(np.mean(crabs))
    fuel = [0, 0]
    for burn in np.add(np.abs(np.subtract(crabs, mean)), 1):
        fuel[0] += np.sum(np.arange(burn))
    for burn in np.add(np.abs(np.subtract(crabs, mean + 1)), 1):
        fuel[1] += np.sum(np.arange(burn))
    return np.min(fuel)


def main():
    crabs = load_data(file_name)
    # Part1
    print(part1(crabs))
    # Part2
    print(part2(crabs))


if __name__ == '__main__':
    main()
