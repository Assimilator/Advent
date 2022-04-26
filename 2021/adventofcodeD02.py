import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    result = input_file.readlines()
    input_file.close()
    return result


def part1(file_lines):
    x = 0
    y = 0

    for line in file_lines:
        if 'forward' in line:
            x += int(line[8:])
        if 'up' in line:
            y -= int(line[3:])
        if 'down' in line:
            y += int(line[5:])
    return x * y


def part2(file_lines):
    x = 0
    y = 0
    aim = 0

    for line in file_lines:
        if 'forward' in line:
            x += int(line[8:])
            y += aim * int(line[8:])
        if 'up' in line:
            aim -= int(line[3:])
        if 'down' in line:
            aim += int(line[5:])
    return x * y


def main():
    file = load_data(file_name)
    print(part1(file))
    print(part2(file))


if __name__ == '__main__':
    main()
