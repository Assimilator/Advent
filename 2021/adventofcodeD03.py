import sys

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()

maxbit = int((len(lines[0])-1))


## Part one
def part1():
    gamma = [0] * (maxbit)
    epsilon = [1] * (maxbit)
    countlines=0
    
    for line in lines:
        countlines += 1
        for i in range(len(line)-1):
            gamma[i] += int(line[i])

    for i in range(len(gamma)):
        if (gamma[i] >= countlines /2):
            gamma[i] = 1
        else:
            gamma[i] = 0
        epsilon[i] -= gamma[i]

    print(int(''.join(str(v) for v in gamma),2)*int(''.join(str(v) for v in epsilon),2))

## Finding the common bits
def part2():
    container = [0] * (maxbit)
    countlines=0
    
    for bit in range(maxbit):
        countlines = 0
        for line in range(len(lines)):
            if (bit > 1):
                stroxy=''.join(str(v) for v in (container[0:bit]))
                if (stroxy == (lines[line][0:bit])):
                    countlines += 1
                    container[bit] += int(lines[line][bit]) 
            elif (bit == 1):
                if (container[bit-1] == int(lines[line][bit-1])):              
                    countlines += 1
                    container[bit] += int(lines[line][bit])       
            else:
                countlines += 1
                container[bit] += int(lines[line][bit])
        if (countlines == 1):
            break
        if (container[bit] >= countlines /2):
            container[bit] = 1
        else:
            container[bit] = 0
    BINcontainer1=''.join(str(v) for v in container)
    DECcontainer1 = int(BINcontainer1,2)

    ## Finding the uncommon bits
    container = [0] * (maxbit)
    for bit in range(maxbit):
        countlines = 0
        for line in range(len(lines)):
            if (bit > 1):
                stroxy=''.join(str(v) for v in (container[0:bit]))
                if (stroxy == (lines[line][0:bit])):
                    countlines += 1
                    container[bit] += int(lines[line][bit]) 
            elif (bit == 1):
                if (container[bit-1] == int(lines[line][bit-1])):              
                    countlines += 1
                    container[bit] += int(lines[line][bit])            
            else:
                countlines += 1
                container[bit] += int(lines[line][bit])
        if (countlines == 1):
            break
        if (container[bit] >= countlines /2):
            container[bit] = 0
        else:
            container[bit] = 1
    BINcontainer2=''.join(str(v) for v in container)
    DECcontainer2 = int(BINcontainer2,2)

    print (DECcontainer1*DECcontainer2)

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()