import sys


def istriangle(sides):
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


def split(line):
    return line.split()


def part1():
    triangles = open(sys.argv[1]).readlines()
    triangles = map(split, triangles)
    triangles = filter(istriangle, triangles)
    return len(triangles)


def fromcols(tris):
    trianges = []
    sidenum = 0
    tri0 = []
    tri1 = []
    tri2 = []
    for side in tris:
        tri0.append(side[0])
        tri1.append(side[1])
        tri2.append(side[2])
        if sidenum == 2:
            trianges.append(tri0)
            trianges.append(tri1)
            trianges.append(tri2)
            tri0 = []
            tri1 = []
            tri2 = []
            sidenum = 0
        else:
            sidenum += 1
    return trianges


def part2():
    triangles = open(sys.argv[1]).readlines()
    triangles = map(split, triangles)
    triangles = fromcols(triangles)
    triangles = filter(istriangle, triangles)
    return len(triangles)

print "Part1: " + str(part1())
print "Part2: " + str(part2())
