import sys

import numpy as np

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def reset():
    dimension = 999
    vent_map = np.zeros((dimension, dimension))
    return vent_map


def load_pairs(file):
    double_index_pairs = []
    input_file = open(file, "r")
    lines = input_file.readlines()
    for line in lines:
        double_index_pairs.append([list(map(int, doubleIndexPair.split(','))) for doubleIndexPair in
                                   line.strip().replace('\n', '').split(' -> ')])
    input_file.close()
    return double_index_pairs


def plot_vents(double_index_pairs, vent_map):
    for doubleIndexPair in double_index_pairs:
        plot_line(vent_map, doubleIndexPair[0], doubleIndexPair[1])


def plot_line(vent_map, begin, end):
    if begin[0] == end[0]:
        i = begin[0]
        for j in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1):
            vent_map[j, i] += 1
    elif begin[1] == end[1]:
        j = begin[1]
        for i in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1):
            vent_map[j, i] += 1


def plot_all_vents(double_index_pairs, vent_map):
    for doubleIndexPair in double_index_pairs:
        plot_every_line(vent_map, doubleIndexPair[0], doubleIndexPair[1])


def plot_every_line(vent_map, begin, end):
    if begin[0] == end[0]:
        i = begin[0]
        for j in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1):
            vent_map[j, i] += 1
    elif begin[1] == end[1]:
        j = begin[1]
        for i in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1):
            vent_map[j, i] += 1
    else:
        for (x, y) in [(i, j) for j in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1) for i in
                       range(min(begin[0], end[0]), max(begin[0], end[0]) + 1)]:
            if (x - begin[0]) * (begin[0] - end[0]) == (y - begin[1]) * (begin[1] - end[1]):
                # print(x, y, begin[0], begin[1], end[0], end[1])
                vent_map[y, x] += 1


def tally_map(vent_map):
    return len(np.nonzero(vent_map > 1)[0])


def main():
    vent_map = reset()
    double_index_pairs = load_pairs(file_name)
    plot_vents(double_index_pairs, vent_map)
    print(tally_map(vent_map))
    vent_map = reset()
    plot_all_vents(double_index_pairs, vent_map)
    print(tally_map(vent_map))


if __name__ == '__main__':
    main()
