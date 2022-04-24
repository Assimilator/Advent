import sys

import numpy as np
import pandas as pd
from scipy import ndimage

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    lines = input_file.readlines()
    df = pd.DataFrame()
    cols = 0
    for line in lines:
        df[str(cols)] = list(str(line.strip().replace('\n', '')))
        cols += 1
    input_file.close()
    return df.T.astype(int).to_numpy()


def find_minima(cave_map):
    return cave_map == ndimage.minimum_filter(cave_map, 3, mode='constant', cval=9)


def part1(cave_map):
    minima = find_minima(cave_map)
    return np.sum(np.where(minima == True, cave_map + 1, 0))


def part2(cave_map):
    # CCL by zeroed ridges, then flattening into 1d
    basins = ndimage.label(np.where((cave_map == 9), 0, 1))[0].flatten()

    # Getting 3 largest non-zero objects
    largest_basins = np.sort(np.unique((np.take(basins, np.where(basins != 0))[0]), return_counts=True)[1])[-3:]
    return np.prod(largest_basins)


def main():
    cave_map = load_data(file_name)
    print(part1(cave_map))
    print(part2(cave_map))


if __name__ == '__main__':
    main()
