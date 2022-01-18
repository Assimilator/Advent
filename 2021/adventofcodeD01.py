import numpy as np
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], header=None)

## Convolve function returns a set of sums of a rolling window
def rollingWindowSum(set, windowSize):
    return np.convolve(set,np.ones(windowSize,dtype=int),'valid')

## Staggered comparison where increases are summed ones
def part1(set):
    x = set[:-1]
    y = set[1:]
    print(sum(np.where(x < y, 1, 0)))
    
## Redoing the comparison with size 3 window
def part2(set):
    part1(rollingWindowSum(set, 3))
    
def main():
    part1(df.T.to_numpy()[0])
    part2(df.T.to_numpy()[0])

if __name__ == '__main__':
    main()