import sys

import numpy as np
import pandas as pd
from scipy.signal import argrelextrema, argrelmin


def main():
    mapDF = pd.read_csv(sys.argv[1], header=None, names=['Col1'])
    mapDF['Col'] =  mapDF['Col1'].astype(str)
    mapDF.drop('Col1', axis=1, inplace=True)
    print(len(mapDF['Col'][0]))
    for i in range(len(mapDF['Col'][0])):
        mapDF['Col'+str(i)] = mapDF['Col'].astype(str).str[i:i+1]
    mapDF.drop('Col', axis=1, inplace=True)
    mapDF = mapDF.astype(int)#.T
    print(mapDF)
    print(pd.DataFrame.idxmin(mapDF))
    map = mapDF.astype(int).to_numpy()
    print(map)
    # print((map.flatten('F')))
    print()
   
    # print(np.array(argrelextrema(map, np.less)))
    # print(np.array(argrelextrema(map, np.greater)))
    
    localMinima = [0] * (0)
    # print(localMinima,[(np.r_[True, map[1:] < map[:-1]] & np.r_[map[:-1] < map[1:], True])])
    for i in range(len(map)):
        line = map[i]
        localMinima = localMinima.append((np.r_[True, line[1:] < line[:-1]] & np.r_[line[:-1] < line[1:], True]))
        # print()
        print(localMinima)
    
    mapT = mapDF.astype(int).T.to_numpy()
    print(mapT)
    
    for i in range(len(mapT)):
        line = mapT[i]
        print(np.r_[True, line[1:] < line[:-1]] & np.r_[line[:-1] < line[1:], True])
    
    # print(s[1:-1][s[1:-1] < s[:-2] and s[1:-1] < s[2:]])
    # print(np.argmin(map[0]))
    # print(np.argmin(map, axis=0))
    # print(np.argmin(map, axis=1))

if __name__ == '__main__':
    main()
