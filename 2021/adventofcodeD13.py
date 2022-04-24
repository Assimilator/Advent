import sys

import numpy as np

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    lines = input_file.readlines()
    input_file.close()
    indices = []
    folds = []
    for line in lines:
        if ',' in line:
            indices.append([int(index) for index in line.strip().replace('\n', '').split(',')])
        elif '=' in line:
            # x and y are converted into axis values
            folds.append([int(fold) for fold in
                          line.strip().replace('\n', '').replace('fold along ', '').replace('y', '1').replace('x',
                                                                                                    '0').split('=')])
    return indices, folds


def draw_sheet(indices):
    sheet = np.zeros(np.amax(indices, axis=0) + 1)
    for index in indices:
        sheet[index[0]][index[1]] += 1
    return sheet


def fold_sheet(sheet, folds, fold_once=0):
    if len(folds) > 0:
        # folded_sheet = []
        fold = folds.pop(0)

        if fold[0] == 1:
            # Vertical fold
            folded_sheet = sheet[:, :fold[1]] + np.flip(sheet[:, fold[1] + 1:], axis=fold[0])
        else:
            # Horizontal fold
            folded_sheet = sheet[:fold[1], :] + np.flip(sheet[fold[1] + 1:, :], axis=fold[0])

        if fold_once == 1:
            # Part1 solution
            return folded_sheet
        else:
            # Part2 solution
            return fold_sheet(folded_sheet.copy(), folds)
    else:
        return sheet


def part1(sheet, folds):
    # Part1
    folded_sheet = fold_sheet(sheet, folds, 1)
    return np.sum(np.count_nonzero(folded_sheet))


def part2(sheet, folds):
    # Part2
    folded_sheet = fold_sheet(sheet, folds)
    # Reorienting image for readability
    image = np.flip((np.where((folded_sheet > 0), '#', ' ')), axis=0)
    rot_img = np.rot90(image, 3)
    return rot_img


def main():
    indices, folds = load_data(file_name)
    sheet = draw_sheet(indices)

    print(part1(sheet.copy(), folds.copy()))

    rot_img = part2(sheet.copy(), folds.copy())
    for row in rot_img:
        print(''.join(row))


if __name__ == '__main__':
    main()
