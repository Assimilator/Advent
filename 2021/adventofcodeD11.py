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
    input_file.close()
    df = pd.DataFrame()
    cols = 0
    for line in lines:
        df[str(cols)] = list(str(line.strip().replace('\n', '')))
        cols += 1
    return df.T.astype(int).to_numpy()


def process_flashes(grid, flashes, flash_count):
    new_flashes = flashes + np.where((grid > 9), 1, 0)
    new_flashes = np.where(new_flashes > 0, 1, 0)
    new_flash_count = np.sum(new_flashes)
    if new_flash_count > flash_count:
        grid += ndimage.correlate(np.subtract(new_flashes, flashes), np.ones(9).reshape(3, 3), mode='constant', cval=0)
        return process_flashes(grid, new_flashes, new_flash_count)
    else:
        return [np.where(grid > 9, 0, grid), flash_count]


def part1(grid):
    flash_count = 0
    for i in range(100):
        grid += 1
        flashed = process_flashes(grid, np.zeros(grid.shape, dtype=int), 0)
        grid = flashed[0]
        flash_count += flashed[1]
    return flash_count


def part2(grid):
    new_flash_count = 0
    step = 1
    max_flash_count = grid.shape[0] * grid.shape[1]
    while new_flash_count < max_flash_count:
        step += 1
        grid += 1
        flashed = process_flashes(grid, np.zeros(grid.shape, dtype=int), 0)
        grid = flashed[0]
        new_flash_count = flashed[1]
    return step


def main():
    grid = load_data(file_name)
    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    main()
