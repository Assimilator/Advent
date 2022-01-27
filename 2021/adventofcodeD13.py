import sys
import numpy as np
from scipy import ndimage


def loadData():
    inputFile = open(sys.argv[1], "r")
    lines=inputFile.readlines()
    indices = []
    folds = []
    for line in lines:
        if ',' in line:
            indices.append([int(index) for index in line.strip().replace('\n','').split(',')])
        elif '=' in line:
            # x and y are converted into axis values
            folds.append([int(fold) for fold in line.strip().replace('\n','').replace('fold along ','').replace('y','1').replace('x','0').split('=')])
    return indices, folds

def drawSheet(indices):
    sheet = np.zeros(np.amax(indices, axis=0)+1)
    for index in indices:
        sheet[index[0]][index[1]] += 1
    return sheet

def foldSheet(sheet, folds, foldOnce = 0):
    if len(folds) > 0:
        foldedSheet = []
        fold = folds.pop(0)
        
        if fold[0] == 1:
            # Vertical fold
            foldedSheet = sheet[:,:fold[1]] + np.flip(sheet[:,fold[1]+1:], axis=fold[0])
        else:
            # Horizontal fold
            foldedSheet = sheet[:fold[1],:] + np.flip(sheet[fold[1]+1:,:], axis=fold[0])
        
        if foldOnce == 1:
            # Part1 solution
            return foldedSheet 
        else:
            # Part2 solution
            return foldSheet(foldedSheet.copy(), folds)
    else:
        return sheet

def main():
    
    indices, folds = loadData()
    sheet = drawSheet(indices)
    
    # Part1
    foldedSheet = foldSheet(sheet.copy(), folds.copy(), 1)
    print(np.sum(np.count_nonzero(foldedSheet)))
    
    # Part2 
    foldedSheet = foldSheet(sheet.copy(), folds.copy())
    image = np.flip((np.where((foldedSheet > 0), '#', ' ' )), axis=0)
    np.set_printoptions(threshold=sys.maxsize)
    print(image)

if __name__ == '__main__':
    main()