import numpy as np
import sys
import re 

global lineCount

def loadData():
    global lineCount
    signals=[]
    lights=[]
    inputFile = open(sys.argv[1], "r")
    lines = inputFile.readlines()
    lineCount = len(lines)
    for line in lines:
        data = [(item) for item in line.strip().replace('\n','').split(' | ')]
        signals = np.concatenate((signals, data[0].split(' ')))
        lights = np.concatenate((lights, data[1].split(' ')))
        
    return ([signals, lights])
    
def tallyFirst(lights):
    length_checker = np.vectorize(len)
    lengths = length_checker(lights)
    print(len(np.nonzero((lengths == 2) | (lengths == 4) | (lengths == 3) | (lengths == 7))[0]))

def decodeRows(signals):
    numbers = []
    for signalRow in signals:
        numbers.append(decodeRow(signalRow))
    return numbers
    
def decodeRow(signalRow):
    
    lengths = np.vectorize(len)(signalRow)
    
    indexGroup235 = np.where(lengths == 5)[0]
    group235 = np.take(signalRow, indexGroup235)
    indexGroup690 = np.where(lengths == 6)[0]
    group690 = np.take(signalRow, indexGroup690)
    
    one = matcher(re.compile('^[a-g]{2}$'), signalRow)
    four = matcher(re.compile('^[a-g]{4}$'), signalRow)
    seven = matcher(re.compile('^[a-g]{3}$'), signalRow)
    eight = matcher(re.compile('^[a-g]{7}$'), signalRow)
    three = matcher(re.compile(regexBuilder(one)), group235)
    group235 = cleanse(group235, three)
    nine = matcher(re.compile(regexBuilder(four)), group690)
    group690 = cleanse(group690, nine)
    six = matcher(re.compile(regexBuilder(one, partial=True)), group690)
    group690 = cleanse(group690, six)
    zero = group690[0]
    five = matcher(re.compile(regexBuilder(((np.intersect1d([[c] for c in one], [[c] for c in six]))[0]))), group235)
    group235 = cleanse(group235, five)
    two = group235[0]
     
    return (zero, one, two, three, four, five, six, seven, eight, nine)
    
def matcher(regX, row):
    for item in row:
        if regX.search(item):
            return item
            break
            
def indexedMatcher(regX, row, maxLength):
    for i in range(len(row)):
        if len(row[i]) == maxLength and regX.search(row[i]):
            return i
            break
    
def regexBuilder(item, partial=False):
    if partial:
        result = '^([^'
        for i in range(len(item)-1):
            result += item[i] + ']+|[^'
        result += item[len(item)-1] + ']+)$'
    else:
        result = '\w*['
        for i in range(len(item)-1):
            result += item + ']+\w*['
        result += item + ']+\w*'
    return result
    
def cleanse(group, item):
    return np.delete(group, np.where(np.char.find(group, item) == 0)[0][0])
    
def decodeLights(lights, numbers):
    sum = 0
    for i in range(len(lights)):
        sum += decodeLightRow(lights[i],numbers[i])
    return sum

def decodeLightRow(lightRow, numberSet):
    set = ''   
    for item in lightRow:       
        set += str(indexedMatcher(re.compile(regexBuilder(item)), numberSet, len(item)))
    return int(set)

def main():
    global lineCount
    data = loadData()
    signals=np.array(data[0]).reshape(lineCount, int(len(data[0])/lineCount))
    lights=np.array(data[1]).reshape(lineCount, int(len(data[1])/lineCount))    
    
    tallyFirst(lights)
    print()
    
    numbers = decodeRows(signals)
    sum = decodeLights(lights, numbers)
    print(sum)

if __name__ == '__main__':
    main()