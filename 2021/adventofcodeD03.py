import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    lines = input_file.readlines()
    input_file.close()
    max_bit = int((len(lines[0]) - 1))
    return lines, max_bit


# Part one
def part1(lines, max_bit):
    gamma = [0] * max_bit
    epsilon = [1] * max_bit
    count_lines = 0

    for line in lines:
        count_lines += 1
        for i in range(len(line) - 1):
            gamma[i] += int(line[i])

    for i in range(len(gamma)):
        if gamma[i] >= count_lines / 2:
            gamma[i] = 1
        else:
            gamma[i] = 0
        epsilon[i] -= gamma[i]

    return int(''.join(str(v) for v in gamma), 2) * int(''.join(str(v) for v in epsilon), 2)


# Finding the common bits
def part2(lines, max_bit):
    container = [0] * max_bit
    count_lines = 0

    for bit in range(max_bit):
        count_lines = 0
        for line in range(len(lines)):
            if bit > 1:
                str_oxygen = ''.join(str(v) for v in (container[0:bit]))
                if str_oxygen == (lines[line][0:bit]):
                    count_lines += 1
                    container[bit] += int(lines[line][bit])
            elif bit == 1:
                if container[bit - 1] == int(lines[line][bit - 1]):
                    count_lines += 1
                    container[bit] += int(lines[line][bit])
            else:
                count_lines += 1
                container[bit] += int(lines[line][bit])
        if count_lines == 1:
            break
        if container[bit] >= count_lines / 2:
            container[bit] = 1
        else:
            container[bit] = 0
    bin_container1 = ''.join(str(v) for v in container)
    dec_container1 = int(bin_container1, 2)

    # Finding the uncommon bits
    container = [0] * max_bit
    for bit in range(max_bit):
        count_lines = 0
        for line in range(len(lines)):
            if bit > 1:
                str_oxygen = ''.join(str(v) for v in (container[0:bit]))
                if str_oxygen == (lines[line][0:bit]):
                    count_lines += 1
                    container[bit] += int(lines[line][bit])
            elif bit == 1:
                if container[bit - 1] == int(lines[line][bit - 1]):
                    count_lines += 1
                    container[bit] += int(lines[line][bit])
            else:
                count_lines += 1
                container[bit] += int(lines[line][bit])
        if count_lines == 1:
            break
        if container[bit] >= count_lines / 2:
            container[bit] = 0
        else:
            container[bit] = 1
    bin_container2 = ''.join(str(v) for v in container)
    dec_container2 = int(bin_container2, 2)

    return dec_container1 * dec_container2


def main():
    lines, max_bit = load_data(file_name)
    print(part1(lines, max_bit))
    print(part2(lines, max_bit))


if __name__ == '__main__':
    main()
