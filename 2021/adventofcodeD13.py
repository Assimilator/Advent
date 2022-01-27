import sys
import numpy as np


def loadData():
    inputFile = open(sys.argv[1], "r")
    lines=inputFile.readlines()
    indices = []
    folds = []
    for line in lines:
        if ',' in line:
            indices.append([int(index) for index in line.strip().replace('\n','').split(',')])
        elif '=' in line:
            #x and y are converted into axis values
            folds.append([int(fold) for fold in line.strip().replace('\n','').replace('fold along ','').replace('y','0').replace('x','1').split('=')])
    return indices, folds

def drawSheet(indices):
    sheet = np.zeros(np.amax(indices, axis=0)+1)
    for index in indices:
        sheet[index[0]][index[1]] += 1
    return sheet

#TODO: complete the method
def foldSheet(sheet, folds):
    foldedSheet = []
    if len(folds) > 0:
        fold = folds.pop(0)
        if fold[0] == 0:
            foldedSheet = sheet[:,:fold[1]] + np.flip(sheet[:,fold[1]+1:], axis=1)
        else:
            foldedSheet = sheet[:fold[1],:] + np.flip(sheet[fold[1]+1:,:], axis=0)
        return foldedSheet #foldSheet(foldedSheet.copy(), folds)   
    else:
        return sheet

def main():
    indices, folds = loadData()
    sheet = drawSheet(indices)
    foldedSheet = foldSheet(sheet.copy(), folds.copy())
    print(np.sum(np.count_nonzero(foldedSheet)))

if __name__ == '__main__':
    main()