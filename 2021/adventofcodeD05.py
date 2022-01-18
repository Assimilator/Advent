import numpy as np
import sys

def reset():
    dimension = 999
    ventMap = np.zeros((dimension, dimension))
    return ventMap

def loadPairs():
    doubleIndexPairs = []
    inputFile = open(sys.argv[1], "r")
    lines=inputFile.readlines()
    for line in lines:
        doubleIndexPairs.append([list(map(int, doubleIndexPair.split(','))) for doubleIndexPair in line.strip().replace('\n','').split(' -> ')])
    return doubleIndexPairs

def plotVents(doubleIndexPairs, ventMap):
    for doubleIndexPair in doubleIndexPairs:
        plotLine(ventMap, doubleIndexPair[0], doubleIndexPair[1])

def plotLine(ventMap, begin, end):    
    if begin[0] == end[0]:
        i = begin[0]
        for j in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1):
            ventMap[j,i] += 1
    elif begin[1] == end[1]:
        j = begin[1]
        for i in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1):
            ventMap[j,i] += 1


def plotAllVents(doubleIndexPairs, ventMap):
    for doubleIndexPair in doubleIndexPairs:        
        plotEveryLine(ventMap, doubleIndexPair[0], doubleIndexPair[1])

def plotEveryLine(ventMap, begin, end):    
    if begin[0] == end[0]:
        i = begin[0]
        for j in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1):
            ventMap[j,i] += 1
    elif begin[1] == end[1]:
        j = begin[1]
        for i in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1):
            ventMap[j,i] += 1
    else:
        for (x, y) in [(i, j) for j in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1) for i in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1) ]:
            if ( (x - begin[0]) * (begin[0] - end[0]) == (y - begin[1]) * (begin[1] - end[1]) ):
                # print(x, y, begin[0], begin[1], end[0], end[1])
                ventMap[y, x] +=1
    
def tallyMap(ventMap):
    return len(np.nonzero(ventMap > 1)[0])

def main():
    ventMap = reset()
    doubleIndexPairs = loadPairs()
    plotVents(doubleIndexPairs, ventMap)
    tally = tallyMap(ventMap)
    print(tally)
    ventMap = reset()
    plotAllVents(doubleIndexPairs, ventMap)
    tally = tallyMap(ventMap)
    print(tally)

if __name__ == '__main__':
    main()
