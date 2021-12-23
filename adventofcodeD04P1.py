import numpy as np
import re

inputFile=open('input8.txt')
numbers=inputFile.readline().split(',')
inputFile.readline()
lines=inputFile.readlines()

global boards
boards = [];

def loadBoards(boards):
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

def play(boards, numbers):
    for num in numbers:
        for boardIndex in range(len(boards)):
            result = checkWin(boardIndex, int(num))
            if result > 0:         
                print(result) 
                break
        if result > 0:         
            break

def checkWin(boardIndex, num):
    # print(num, boardIndex+1)
    indices = np.where(boards[boardIndex] == num)
    sum=0
    if(np.size(indices)):
        y=indices[1][0]
        x=indices[2][0]
        boards[boardIndex][1][y][x]=0
        
        sums1 = np.sum(boards[boardIndex], axis=1)
        win1 = np.where(sums1 == 0)
        if(np.any(win1)):
            # print(sums1)
            sum = calcVictory(boardIndex, num, x, y)            
        else:
            sums2 = np.sum(boards[boardIndex], axis=2)
            win2 = np.where(sums2 == 0)
            if(np.any(win2)):
                # print(sums2)
                sum = calcVictory(boardIndex, num, x, y)
    # print(sum, num)
    return sum*num
    
def calcVictory(boardIndex, num, x, y):
    sum=0
    # print(boards[boardIndex])
    for i in range(5):
        for j in range(5):
            if (boards[boardIndex][1][i][j] < 0):
                sum += boards[boardIndex][0][i][j]
    return sum

def main():
    loadBoards(boards)
##    print('\n-- boards --\n')
##    print(boards)
    play(boards, numbers)

if __name__ == '__main__':
    main()
