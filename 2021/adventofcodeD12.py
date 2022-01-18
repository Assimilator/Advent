import sys
import numpy as np
import pandas as pd
from scipy import ndimage


def loadData():
    return pd.read_csv(sys.argv[1], header=None).to_numpy()

def main():
    rows = loadData()    
    processRows(rows)    

if __name__ == '__main__':
    main()