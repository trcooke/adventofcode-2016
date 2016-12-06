import sys


def getname(line):
    chars = line[0:line.rfind("-")].replace("-", "")
    occs = {i: chars.count(i) for i in chars}
    count = {}
    for occ in occs:
        chr = []
        if occs[occ] in count:
            chr = count[occs[occ]]
            chr.append(occ)
        else:
            chr = [occ]
        count[occs[occ]] = chr
    srt = ""
    for w in sorted(count, reverse=True):
        srt += "".join(sorted(count[w]))
    return srt


def getsector(line):
    return int(line[line.rfind("-") + 1:line.find("[")])


def getcheck(line):
    return line[line.find("[") + 1:line.find("]")]


def part1():
    triangles = open(sys.argv[1]).readlines()
    sectorsum = 0
    for line in triangles:
        name = getname(line)
        sector = getsector(line)
        check = getcheck(line)
        if name[0:5] == check:
            sectorsum += sector
    return sectorsum


def part2():
    return 0


print "Part1: " + str(part1())
print "Part2: " + str(part2())
