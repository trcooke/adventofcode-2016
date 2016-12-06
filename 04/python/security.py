import sys


def getname(line):
    return line[0:line.rfind("-")]


def getcommonletters(name):
    occs = {i: name.count(i) for i in name}
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
    lines = open(sys.argv[1]).readlines()
    sectorsum = 0
    for line in lines:
        name = getname(line).replace("-", "")
        commonletters = getcommonletters(name)
        sector = getsector(line)
        check = getcheck(line)
        if commonletters[0:5] == check:
            sectorsum += sector
    return sectorsum


def decryptname(name, shift):
    decrypted = ""
    for char in name:
        if char == "-":
            decrypted += " "
        else:
            decrypted += chr(((ord(char) - 97 + shift) % 26) + 97)
    return decrypted


def part2():
    lines = open(sys.argv[1]).readlines()
    validlines = []
    for line in lines:
        name = getname(line).replace("-", "")
        commonletters = getcommonletters(name)
        check = getcheck(line)
        if commonletters[0:5] == check:
            validlines.append(line)
    for validline in validlines:
        name = getname(validline)
        sector = getsector(validline)
        decrypted = decryptname(name, sector)
        if "northpole" in decrypted:
            return sector


print "Part1: " + str(part1())
print "Part2: " + str(part2())
