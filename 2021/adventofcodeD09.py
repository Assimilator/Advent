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

def fMinima(map):
    return (map == ndimage.minimum_filter(map, 3, mode='constant', cval=9))
        
def part1(map):
    mins = fMinima(map)
    print(np.sum(np.where( mins == True, map+1, 0)))

def part2(map):
    # CCL by zeroed ridges, then flattening into 1d
    basins = ndimage.label(np.where((map == 9), 0, 1 ))[0].flatten()
    
    # Getting 3 largest non-zero objects
    lBasins = np.sort(np.unique((np.take(basins,np.where(basins != 0))[0]), return_counts=True)[1])[-3:]
    print(np.prod(lBasins))

def main():
    map = loadData()
    part1(map)
    part2(map)

if __name__ == '__main__':
    main()