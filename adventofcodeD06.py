import numpy as np
import sys
from functools import lru_cache

def loadData():
    inputFile = open(sys.argv[1], "r")
    fishies = [(int(item)) for item in inputFile.readline().strip().replace('\n','').split(',')]
    return fishies

global days 
days = 256
    
@lru_cache(1024)
def fishPop(d = 0, t = 8):
    global days
    fishCount = 0
    for i in range(d, days):
        if t == 0:
            t = 7
            fishCount += 1 + fishPop(i + 1)
        t -= 1
    return fishCount

def main():
    fishies = loadData()
    fishCount = len(fishies)
    for fish in fishies:        
        fishCount += fishPop(0,fish)
    print(fishCount)

if __name__ == '__main__':
    main()