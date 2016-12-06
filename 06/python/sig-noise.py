import sys


def part1():
    lines = open(sys.argv[1]).readlines()
    cols = [[],[],[],[],[],[],[],[]]
    message = ""
    for line in lines:
        for i in range(8):
            cols[i].append(line[i])
    for col in cols:
        highest = ""
        highocc = 0
        for chr in col:
            occ = col.count(chr)
            if occ > highocc:
                highest = chr
                highocc = occ
        message += highest
        print message
    return message


def part2():
    lines = open(sys.argv[1]).readlines()
    cols = [[],[],[],[],[],[],[],[]]
    message = ""
    for line in lines:
        for i in range(8):
            cols[i].append(line[i])
    for col in cols:
        lowest = ""
        lowocc = 1000
        for chr in col:
            occ = col.count(chr)
            if occ < lowocc:
                lowest = chr
                lowocc = occ
        message += lowest
        print message
    return message


print "Part1: " + str(part1())
print "Part2: " + str(part2())