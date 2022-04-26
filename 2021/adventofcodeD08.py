import re
import sys

import numpy as np

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    signals = []
    lights = []
    input_file = open(file, "r")
    lines = input_file.readlines()
    line_count = len(lines)
    for line in lines:
        data = [item for item in line.strip().replace('\n', '').split(' | ')]
        signals = np.concatenate((signals, data[0].split(' ')))
        lights = np.concatenate((lights, data[1].split(' ')))
    signals = np.array(signals).reshape(line_count, int(len(signals) / line_count))
    lights = np.array(lights).reshape(line_count, int(len(lights) / line_count))
    input_file.close()
    return [signals, lights]


def tally_first(lights):
    length_checker = np.vectorize(len)
    lengths = length_checker(lights)
    return len(np.nonzero((lengths == 2) | (lengths == 4) | (lengths == 3) | (lengths == 7))[0])


def decode_rows(signals):
    numbers = []
    for signal_row in signals:
        numbers.append(decode_row(signal_row))
    return numbers


def decode_row(signal_row):
    lengths = np.vectorize(len)(signal_row)

    index_group_235 = np.where(lengths == 5)[0]
    group_235 = np.take(signal_row, index_group_235)
    index_group_690 = np.where(lengths == 6)[0]
    group_690 = np.take(signal_row, index_group_690)

    one = matcher(re.compile('^[a-g]{2}$'), signal_row)
    four = matcher(re.compile('^[a-g]{4}$'), signal_row)
    seven = matcher(re.compile('^[a-g]{3}$'), signal_row)
    eight = matcher(re.compile('^[a-g]{7}$'), signal_row)
    three = matcher(re.compile(regex_builder(one)), group_235)
    group_235 = cleanse(group_235, three)
    nine = matcher(re.compile(regex_builder(four)), group_690)
    group_690 = cleanse(group_690, nine)
    six = matcher(re.compile(regex_builder(one, partial=True)), group_690)
    group_690 = cleanse(group_690, six)
    zero = group_690[0]
    five = matcher(re.compile(regex_builder(((np.intersect1d([[c] for c in one], [[c] for c in six]))[0]))), group_235)
    group_235 = cleanse(group_235, five)
    two = group_235[0]

    return zero, one, two, three, four, five, six, seven, eight, nine


def matcher(reg_x, row):
    for item in row:
        if reg_x.search(item):
            return item


def indexed_matcher(reg_x, row, max_length):
    for i in range(len(row)):
        if len(row[i]) == max_length and reg_x.search(row[i]):
            return i


def regex_builder(item, partial=False):
    if partial:
        result = '^([^'
        for i in range(len(item) - 1):
            result += item[i] + ']+|[^'
        result += item[len(item) - 1] + ']+)$'
    else:
        result = '\w*['
        for i in range(len(item) - 1):
            result += item + ']+\w*['
        result += item + ']+\w*'
    return result


def cleanse(group, item):
    return np.delete(group, np.where(np.char.find(group, item) == 0)[0][0])


def decode_lights(lights, numbers):
    decoded_sum = 0
    for i in range(len(lights)):
        decoded_sum += decode_light_row(lights[i], numbers[i])
    return decoded_sum


def decode_light_row(light_row, number_set):
    decoded_set = ''
    for item in light_row:
        decoded_set += str(indexed_matcher(re.compile(regex_builder(item)), number_set, len(item)))
    return int(decoded_set)


def main():
    signals, lights = load_data(file_name)
    # Part1
    print(tally_first(lights))
    # Part2
    print(decode_lights(lights, decode_rows(signals)))


if __name__ == '__main__':
    main()
