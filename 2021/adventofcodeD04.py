import re
import sys

import numpy as np

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    numbers = input_file.readline().split(',')
    input_file.readline()
    lines = input_file.readlines()
    input_file.close()
    return numbers, lines


def load_boards(lines):
    boards = []
    i = 0
    board = np.zeros((2, 5, 5)).astype(int)
    board.fill(-1)
    for line in lines:
        if line not in '\n':
            stripped = line.replace('\n', '').strip()
            row = (re.split(' +', stripped))
            for j in range(5):
                board[0][i][j] = row[j]
            i += 1
        if i == 5:
            i = 0
            boards.append(board)
            board = np.zeros((2, 5, 5)).astype(int)
            board.fill(-1)
    return boards


def play_p1(boards, numbers):
    board_list = [1] * len(boards)
    result = 0
    for num in numbers:
        for board_index in range(len(boards)):
            result = check_win(boards, board_index, int(num), board_list)
            if result > 0:
                return result
        if result > 0:
            break


def play_p2(boards, numbers):
    board_list = [1] * len(boards)
    result = 0
    for num in numbers:
        for board_index in range(len(boards)):
            result = check_win(boards, board_index, int(num), board_list)
            if result > 0 and not np.any(board_list):
                return result
        if result > 0 and not np.any(board_list):
            break


def check_win(boards, board_index, num, board_list):
    indices = np.where(boards[board_index] == num)
    unmarked_sum = 0
    if np.size(indices):
        y = indices[1][0]
        x = indices[2][0]
        boards[board_index][1][y][x] = 0

        sums1 = np.sum(boards[board_index], axis=1)
        win1 = np.where(sums1 == 0)
        if np.any(win1):
            board_list[board_index] = 0
            unmarked_sum = calc_victory(boards, board_index)
        else:
            sums2 = np.sum(boards[board_index], axis=2)
            win2 = np.where(sums2 == 0)
            if np.any(win2):
                board_list[board_index] = 0
                unmarked_sum = calc_victory(boards, board_index)
    return unmarked_sum * num


def calc_victory(boards, board_index):
    unmarked_sum = 0
    for i in range(5):
        for j in range(5):
            if boards[board_index][1][i][j] < 0:
                unmarked_sum += boards[board_index][0][i][j]
    return unmarked_sum


def main():
    numbers, lines = load_data(file_name)
    boards = load_boards(lines)
    print(play_p1(boards, numbers))
    print(play_p2(boards, numbers))


if __name__ == '__main__':
    main()
