import sys
from collections import deque


def shiftright(grid, rowindex, by):
    row = grid[rowindex]
    for i in range(by):
        tmp = row.pop()
        row.appendleft(tmp)
    grid[rowindex] = row
    return grid


def shiftdown(grid, colindex, by):
    col = deque()
    for i in range(6):
        col.append(grid[i][colindex])
    for i in range(by):
        tmp = col.pop()
        col.appendleft(tmp)
    for i in range(6):
        grid[i][colindex] = col.popleft()
    return grid


def applyinstruction(instruction, grid):
    if instruction.startswith("rect "):
        rect = instruction[5:].split("x")
        for row in range(int(rect[1])):
            for col in range(int(rect[0])):
                grid[row][col] = "o"
    elif "y=" in instruction:
        rowindex = int(instruction[instruction.find("y=") + 2:instruction.find(" ", instruction.find("y=") + 2)])
        by = int(instruction[instruction.find("by") + 3:])
        print "Rotate row " + instruction
        grid = shiftright(grid, rowindex, by)
    else:
        colindex = int(instruction[instruction.find("x=") + 2:instruction.find(" ", instruction.find("x=") + 2)])
        by = int(instruction[instruction.find("by") + 3:])
        print "Rotate col " + instruction
        grid = shiftdown(grid, colindex, by)
    return grid


def printgrid(grid):
    for row in grid:
        print "".join(row)
    print ""


def part1():
    grid = []
    for i in range(6):
        row = deque()
        for col in range(50):
            row.append(".")
        grid.append(row)
    printgrid(grid)

    lines = open(sys.argv[1]).readlines()
    for line in lines:
        grid = applyinstruction(line, grid)
        printgrid(grid)
    count = 0
    for row in grid:
        count += row.count("o")
    return count


print "Part1: " + str(part1())
