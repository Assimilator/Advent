import sys
import numpy as np
import pandas as pd
from functools import lru_cache


openB =   np.array(['(','[','{','<'])
closeB =  np.array([')',']','}','>'])
points =  np.array([3, 57, 1197, 25137])
pointsB = np.array([1, 2, 3, 4])

def loadData():
    return pd.read_csv(sys.argv[1], header=None).to_numpy()
    
def processRows(rows):
    illegals = []
    incompletes = []
    totals = []
    for row in rows:
        candidate = processRow(row.astype(str)[0])
        processRow.cache_clear()
        if candidate[0] == -1:
            illegals.append(candidate[1])
        else:
            incompletes.append((candidate[1]))
    print(np.sum(illegals))
    print(int(np.median(incompletes)))
    
@lru_cache(256)
def processRow(row):
    if len(row) == 0:
        return [0, 0]
    elif row[0] in openB:
        oIndex = np.where(openB == row[0])[0][0]
        
        trail = processRow(row[1:])
        if trail[0] == 0:            
            trail[1] = trail[1] * 5 + pointsB[oIndex]
            return [0, trail[1]]
        elif trail[0] == -1:
            return trail 
        else:
            cIndex = np.where(closeB == trail[0])[0][0]
            if oIndex == cIndex:
                return processRow(trail[1:])
            else:
                return [-1, points[np.where(closeB == trail[0])[0]]]
    else:
        return row

def main():
    rows = loadData()    
    processRows(rows)    

if __name__ == '__main__':
    main()