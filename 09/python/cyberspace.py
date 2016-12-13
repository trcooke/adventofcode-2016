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
    return len(decompressed)


def decompress2(inp):
    count = 0
    while inp.find("(") != -1:
        count += len(inp[:inp.find("(")])
        instr = inp[inp.find("(") + 1:inp.find(")")].split("x")
        sectionboundaries = (inp.find(")") + 1, inp.find(")") + 1 + int(instr[0]))
        decompsection = inp[sectionboundaries[0]:sectionboundaries[1]] * int(instr[1])
        rest = inp[sectionboundaries[1]:]
        inp = decompsection + rest
    count += len(inp)
    return count


def part2():
    line = open(sys.argv[1]).readlines()[0].replace("\n","")
    decompressed = decompress2(line)
    return decompressed


print "Part1(): " + str(part1())
print "Part2(): " + str(part2())
