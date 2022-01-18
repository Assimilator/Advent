import array
import sys

inputFile = open(sys.argv[1], "r")
file = inputFile.readlines()    

def part1():
    x=0
    y=0

    for line in file:
        if('forward' in line):
            x += int(line[8:])
        if('up' in line):
            y -= int(line[3:])
        if('down' in line):
            y += int(line[5:])
    print(x*y)

def part2():
    x=0
    y=0
    aim=0

    for line in file:
        if('forward' in line):
            x += int(line[8:])
            y += aim*int(line[8:])
        if('up' in line):
            aim -= int(line[3:])
        if('down' in line):
            aim += int(line[5:])
    print(x*y)

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()