import numpy as np
import sys

def loadData():
    inputFile = open(sys.argv[1], "r")
    crabs = [(int(item)) for item in inputFile.readline().strip().replace('\n','').split(',')]
    return crabs

def main():
    crabs = loadData()
    
    median = int(np.median(crabs))
    fuel = [0,0]
    fuel[0] = np.sum(np.abs(np.subtract(crabs, median)))
    fuel[1] = np.sum(np.abs(np.subtract(crabs, median+1)))
    print(np.min(fuel))
    
    mean = int(np.mean(crabs))
    fuel = [0,0]
    for burn in np.add(np.abs(np.subtract(crabs, mean)),1):
        fuel[0] += np.sum(np.arange(burn))
    for burn in np.add(np.abs(np.subtract(crabs, mean+1)),1):
        fuel[1] += np.sum(np.arange(burn))
    print(np.min(fuel))

if __name__ == '__main__':
    main()