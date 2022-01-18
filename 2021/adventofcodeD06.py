import numpy as np
import sys
from functools import lru_cache


def loadData():
    inputFile = open(sys.argv[1], "r")
    fishies = [(int(item)) for item in inputFile.readline().strip().replace('\n','').split(',')]
    return fishies

@lru_cache(256)
def fishPop(days, d = 0, t = 8):
    fishCount = 0
    for i in range(d, days):
        if t == 0:
            t = 7
            fishCount += 1 + fishPop(days, i + 1)
        t -= 1
    return fishCount

def main():
    fishies = loadData()
    # Part1
    fishCount = len(fishies)
    for fish in fishies:        
        fishCount += fishPop(80, 0,fish)
    print(fishCount)
    # Part2
    fishCount = len(fishies)
    for fish in fishies:        
        fishCount += fishPop(256, 0,fish)
    print(fishCount)

if __name__ == '__main__':
    main()