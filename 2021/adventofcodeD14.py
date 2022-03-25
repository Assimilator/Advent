import numpy as np
import sys

# Optimization
# import timeit

import matplotlib.pyplot as plt

# AI
import pandas as pd
import statsmodels.formula.api as smf

def loadPolymers():
    inputFile = open(sys.argv[1], "r")
    polymers = inputFile.readline().strip().replace('\n','').split()
    return ([ c for c in polymers[0]])
    
def loadRules():
    inputFile = open(sys.argv[1], "r")
    inputFile.readline()
    inputFile.readline()
    rules = [[[c for c in pair[0]], pair[1]] for pair in [(item.strip().replace('\n','').split(' -> ')) for item in inputFile.readlines()]]
    return rules
    
def rolling_window(array, window=2):
    shape = array.shape[:-1] + (array.shape[-1] - window + 1, window)
    strides = array.strides + (array.strides[-1],)
    return np.lib.stride_tricks.as_strided(array, shape=shape, strides=strides)

def main():
    polymers = np.array(loadPolymers())
    print(''.join(polymers))
    
    rules = loadRules()
    list1 = []
    list2 = []
    list3 = []
    
    # Redo as recursion
    for step in range(10):
        # print(step)
        # offset = 0
        newPolyIndices = np.zeros(0, dtype=int)
        newPolyValues = np.zeros(0)
        for rule in rules:
            
            # This needs to be multithreaded
            indices = np.all(rolling_window(polymers) == rule[0], axis=1)
            
            ruleIndices = (np.mgrid[0:len(indices)][indices]).astype(int) +1
            
            # ruleValues = ruleIndices.copy().astype('str')
            # ruleValues.fill(rule[1])
            
            # These two need to be cached
            newPolyIndices = np.concatenate((newPolyIndices, ruleIndices), dtype=int)
            newPolyValues = np.concatenate(newPolyValues, [(rule[1]) for i in ruleIndices])
           
            # Optimization
            # print(timeit.timeit(lambda: [(rule[1]) for i in ruleIndices], number=1))            
            # print(timeit.timeit(lambda: ruleIndices.astype('str').fill(rule[1]), number=1))
            
            # break
                
        # print(newPolyIndices, newPolyValues)
    
        # break
        polymers = np.insert(polymers, newPolyIndices, newPolyValues)
        
        # Debugging
        # print('poly:', polymers)
        counts = np.unique(polymers, return_counts=True)
        
        # print(counts)
        print(step+1, np.max(counts[1]), np.min(counts[1]), np.max(counts[1]) - np.min(counts[1]))
        list1.append([step+1, np.max(counts[1])])
        list2.append([step+1, np.min(counts[1])])
        list3.append([step+1, np.max(counts[1]) - np.min(counts[1])])
        
        # Plotting
        # plt.style.use('_mpl-gallery')
        # x = 0.5 + np.arange(8)
        # y = np.random.uniform(2, 7, len(x))
        # plot
        # fig, ax = plt.subplots()
        # ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
               # ylim=(0, 8), yticks=np.arange(1, 8))
        # plt.show()
        # plt.savefig('plot.png')
    print(list1)
    
    # AI model training
    df1 = pd.DataFrame(list1, columns = ['steps','pol_values'])
    df2 = pd.DataFrame(list2, columns = ['steps','pol_values'])
    df3 = pd.DataFrame(list3, columns = ['steps','pol_values'])
    
    formula = "pol_values ~ steps"
    
    model = smf.ols(formula = formula, data = df1).fit()
    
    # print("Intercept:", model.params[0], "Slope:", model.params[1])
    print("R-squared:", model.rsquared)
    
    
    # Debugging
    # print(df1)
    # print(df1.steps, df1.pol_values)
    # print(df2)
    print(df3)
    print(np.count_nonzero((polymers)))
    
    
    plt.figure(figsize=(4, 3))
    # ax = plt.axes()
    # ax.scatter(df1.steps, df1.pol_values)
    # ax.plot(x_new, y_new)  
    plt.scatter(df1.steps, df1.pol_values, color='blue')
    plt.scatter(df2.steps, df2.pol_values, color='green')
    plt.scatter(df3.steps, df3.pol_values, color='red')
    plt.show()
    plt.savefig('plot.png')
    
    counts = np.unique(polymers, return_counts=True)
    print(counts)
    print(np.max(counts[1]) - np.min(counts[1]))

if __name__ == '__main__':
    main()