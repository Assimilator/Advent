import sys
import numpy as np
import pandas as pd
from scipy import ndimage


def loadData():
    lines = open(sys.argv[1], "r").readlines()
    df = pd.DataFrame()
    cols = 0
    for line in lines:
        df[str(cols)] = list(str(line.strip().replace('\n','')))
        cols+=1
    return(df.T.astype(int).to_numpy())

def processFlashes(grid, flashes, flashCount):
    newFlashes = flashes + np.where((grid > 9), 1, 0 )
    newFlashes = np.where(newFlashes > 0, 1, 0)
    newFlashCount = np.sum(newFlashes)
    if newFlashCount > flashCount:
        grid += ndimage.correlate(np.subtract(newFlashes, flashes), np.ones(9).reshape(3,3), mode='constant', cval=0)
        return processFlashes(grid, newFlashes, newFlashCount)
    else:
        return [np.where(grid > 9, 0, grid), flashCount]

def part1(grid):
    flashCount = 0    
    for i in range(100):
        grid += 1
        flashed = processFlashes(grid, np.zeros(grid.shape, dtype=int), 0)
        grid = flashed[0]
        flashCount += flashed[1]
    print(flashCount)

def part2(grid):
    newFlashCount = 0
    step = 1
    maxFlashCount = grid.shape[0]*grid.shape[1]
    while newFlashCount < maxFlashCount:
        step += 1
        grid += 1
        flashed = processFlashes(grid, np.zeros(grid.shape, dtype=int), 0)
        grid = flashed[0]
        newFlashCount = flashed[1]
    print(step)

def main():
    grid = loadData()
    test = np.zeros(grid.shape, dtype=int)
    part1(grid)
    part2(grid)

if __name__ == '__main__':
    main()