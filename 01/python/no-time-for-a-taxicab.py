import sys


def moveto(loc, move):
    dir = move[0:1]
    dis = int(move[1:])
    if dir == 'L':
        new_dir = (loc['dir'] - 90) % 360
    elif dir == 'R':
        new_dir = (loc['dir'] + 90) % 360
    else:
        new_dir = loc['dir']

    if new_dir == 0:
        p = loc['p'] + dis
        q = loc['q']
    elif new_dir == 90:
        p = loc['p']
        q = loc['q'] + dis
    elif new_dir == 180:
        p = loc['p'] - dis
        q = loc['q']
    elif new_dir == 270:
        p = loc['p']
        q = loc['q'] - dis
    else:
        p = loc['p']
        q = loc['q']
    return {'dir': new_dir, 'p': p, 'q': q}


def to_granular(dirs):
    moves = []
    for move in dirs:
        dir = move[0:1]
        dis = int(move[1:])
        moves.append(dir + "1")
        dis -= 1
        while dis > 0:
            moves.append("S1")
            dis -= 1
    return moves


def part1():
    directions = open(sys.argv[1]).read().split(", ")
    currentlocation = {'dir': 0, 'p': 0, 'q': 0}
    for move in directions:
        currentlocation = moveto(currentlocation, move)
    return abs(currentlocation['p']) + abs(currentlocation['q'])


def part2():
    directions = open(sys.argv[1]).read().split(", ")
    history = [{'p': 0, 'q': 0}]
    current_location = {'dir': 0, 'p': 0, 'q': 0}
    for move in to_granular(directions):
        current_location = moveto(current_location, move)
        if {'p': current_location['p'], 'q': current_location['q']} in history:
            break
        else:
            history.append({'p': current_location['p'], 'q': current_location['q']})
    return abs(current_location['p']) + abs(current_location['q'])


print "Part1: " + str(part1())
print "Part2: " + str(part2())
