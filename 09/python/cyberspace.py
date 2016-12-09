import sys


def decompress1(inp):
    output = ""
    while inp.find("(") != -1:
        output += inp[:inp.find("(")]
        instr = inp[inp.find("(") + 1:inp.find(")")].split("x")
        output += inp[inp.find(")") + 1:inp.find(")") + 1 + int(instr[0])] * int(instr[1])
        inp = inp[inp.find(")") + 1 + int(instr[0]):]
    output += inp
    return output


def part1():
    line = open(sys.argv[1]).readlines()[0]
    decompressed = decompress1(line)
    print decompressed
    return len(decompressed)


print "Part1(): " + str(part1())
