import sys


def istriangle(t):
    sides = t.split()
    side1 = int(sides[0])
    side2 = int(sides[1])
    side3 = int(sides[2])
    if side1 + side2 <= side3:
        return False
    if side1 + side3 <= side2:
        return False
    if side3 + side2 <= side1:
        return False
    return True


def part1():
    triangles = open(sys.argv[1]).readlines()
    validtriangles = filter(istriangle, triangles)
    return len(validtriangles)


def part2():
    verticaltriangles = open(sys.argv[1]).readlines()


print "Part1: " + str(part1())
print "Part2: " + str(part2())
