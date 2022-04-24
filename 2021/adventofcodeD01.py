import sys

import numpy as np
import pandas as pd

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    return pd.read_csv(file, header=None).T.to_numpy()[0]


# Convolve function returns a set of sums of a rolling window
def rolling_window_sum(full_set, window_size):
    return np.convolve(full_set, np.ones(window_size, dtype=int), 'valid')


# Staggered comparison where increases are summed ones
def part1(full_set):
    x = full_set[:-1]
    y = full_set[1:]
    return sum(np.where(x < y, 1, 0))


# Redoing the comparison with size 3 window
def part2(full_set):
    return part1(rolling_window_sum(full_set, 3))


def main():
    df = load_data(file_name)
    print(part1(df))
    print(part2(df))


if __name__ == '__main__':
    main()
