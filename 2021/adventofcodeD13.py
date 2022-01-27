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
            #TODO: verify that the fold axis replacement is correct
            folds.append([int(fold) for fold in line.strip().replace('\n','').replace('fold along ','').replace('y','0').replace('x','1').split('=')])
    return indices, np.array(folds)

def drawSheet(indices):
    sheet = np.zeros(np.amax(indices, axis=0)+1)
    for index in indices:
        # print(index)
        sheet[index[0]][index[1]] += 1
    return sheet

#TODO: complete the method
def foldSheet(sheet, folds):
    return 0

def main():
    indices, folds = loadData()    
    sheet = drawSheet(indices)
    foldCount = foldSheet(sheet, folds)
    print(foldCount)

if __name__ == '__main__':
    main()