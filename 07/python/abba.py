import sys


def getnexthnet(text, nets, hnets):
    nextrb = text.find("]")
    if nextrb == -1:
        return nets, hnets + [text]
    return getnextnet(text[nextrb+1:], nets, hnets + [text[:nextrb]])


def getnextnet(text, nets, hnets):
    nextlb = text.find("[")
    if nextlb == -1:
        return nets + [text], hnets
    return getnexthnet(text[nextlb+1:], nets + [text[:nextlb]], hnets)


def getnets(text):
    return getnextnet(text, [], [])


def isabba(text):
    for i in range(len(text) - 3):
        if text[i] != text[i+1] and text[i] == text[i+3] and text[i+1] == text[i+2]:
            return True
    return False


def supportstls(line):
    nets = getnets(line)
    abbanets = filter(isabba, nets[0])
    abbahypernets = filter(isabba, nets[1])
    if len(abbanets) != 0 and len(abbahypernets) == 0:
        return True
    return False


def part1():
    lines = open(sys.argv[1]).readlines()
    valid = filter(supportstls, lines)
    return len(valid)


def supportssl(line):
    nets = getnets(line)
    for net in nets[0]:
        for i in range(len(net) - 2):
            if net[i] != net[i+1] and net[i] == net[i+2]:
                for hnet in nets[1]:
                    for j in range(len(hnet) - 2):
                        if hnet[j] == hnet[j+2] == net[i+1] and hnet[j+1] == net[i]:
                            return True
    return False


def part2():
    lines = open(sys.argv[1]).readlines()
    valid = filter(supportssl, lines)
    return len(valid)


print "Part1: " + str(part1())
print "Part2: " + str(part2())