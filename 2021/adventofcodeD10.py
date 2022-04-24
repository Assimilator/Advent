import sys
from functools import lru_cache

import numpy as np
import pandas as pd

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""

openB = np.array(['(', '[', '{', '<'])
closeB = np.array([')', ']', '}', '>'])
points = np.array([3, 57, 1197, 25137])
pointsB = np.array([1, 2, 3, 4])
illegal = 1


def load_data(file):
    return pd.read_csv(file, header=None).to_numpy()


def process_rows(rows):
    illegals = []
    incompletes = []
    for row in rows:
        candidate = process_row(row.astype(str)[0])
        process_row.cache_clear()
        # print(candidate[0])
        if candidate[0] == illegal:
            illegals.append(candidate[1])
        else:
            incompletes.append((candidate[1]))
    return [np.sum(illegals), int(np.median(incompletes))]


@lru_cache(256)
def process_row(row):
    if len(row) == 0:
        return [0, 0]
    elif row[0] in openB:
        o_index = np.where(openB == row[0])[0][0]
        trail = process_row(row[1:])
        # print(trail[0])
        if trail[0] == 0:
            trail[1] = trail[1] * 5 + pointsB[o_index]
            # print(trail[1])
            return [0, trail[1]]
        elif trail[0] == illegal:
            return trail
        else:
            c_index = np.where(closeB == trail[0])[0][0]
            if o_index == c_index:
                return process_row(trail[1:])
            else:
                return [illegal, points[np.where(closeB == trail[0])[0]]]
    else:
        return row


def main():
    rows = load_data(file_name)
    part1, part2 = process_rows(rows)
    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
