import sys
import numpy as np
import re


def loadData():
    inputFile = open(sys.argv[1], "r")
    numbers=inputFile.readline().split(',')
    inputFile.readline()
    lines=inputFile.readlines()
    return numbers, lines

def loadBoards(lines):
    boards = []
    i=0
    board = np.zeros((2, 5, 5)).astype(int)
    board.fill(-1)
    for line in lines:
        if line not in '\n':
            stripped=line.replace('\n','').strip()
            row=(re.split(' +',stripped))
            for j in range(5):
                board[0][i][j]=row[j]
            i+=1
        if (i == 5):
            i=0
            boards.append(board)
            board = np.zeros((2, 5, 5)).astype(int)
            board.fill(-1)
    return boards

def playP1(boards, numbers):
    boardList = [1] * len(boards)
    for num in numbers:
        for boardIndex in range(len(boards)):
            result = checkWin(boards, boardIndex, int(num), boardList)
            if result > 0:         
                print(result) 
                break
        if result > 0:         
            break

def playP2(boards, numbers):
    boardList = [1] * len(boards)
    for num in numbers:
        for boardIndex in range(len(boards)):
            result = checkWin(boards, boardIndex, int(num), boardList)
            if (result > 0 and not np.any(boardList)): 
                print(result)
                break
        if (result > 0 and not np.any(boardList)):
            break

def checkWin(boards, boardIndex, num, boardList):
    indices = np.where(boards[boardIndex] == num)
    sum=0
    if(np.size(indices)):
        y=indices[1][0]
        x=indices[2][0]
        boards[boardIndex][1][y][x]=0
        
        sums1 = np.sum(boards[boardIndex], axis=1)
        win1 = np.where(sums1 == 0)
        if(np.any(win1)):
            boardList[boardIndex]=0
            sum = calcVictory(boards, boardIndex, num, x, y)            
        else:
            sums2 = np.sum(boards[boardIndex], axis=2)
            win2 = np.where(sums2 == 0)
            if(np.any(win2)):
                boardList[boardIndex]=0
                sum = calcVictory(boards, boardIndex, num, x, y)
    return sum*num
    
def calcVictory(boards, boardIndex, num, x, y):
    sum=0
    for i in range(5):
        for j in range(5):
            if (boards[boardIndex][1][i][j] < 0):
                sum += boards[boardIndex][0][i][j]
    return sum

def main():
    numbers, lines = loadData()
    boards = loadBoards(lines)    
    playP1(boards, numbers)
    playP2(boards, numbers)

if __name__ == '__main__':
    main()
