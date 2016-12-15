import sys

bots = {}
answers = {"part1": "", "part2": 1}


def part1():
    lines = open(sys.argv[1]).readlines()
    for line in lines:
        words = line.split()
        if words[0] == "bot":
            if words[0] + words[1] in bots:
                bot = bots[words[0] + words[1]]
            else:
                bot = Bot(words[0] + words[1])
            if words[5] + words[6] in bots:
                if words[5] == "bot":
                    bot.low = words[5] + words[6]
            else:
                if words[5] == "bot":
                    bots[words[5] + words[6]] = Bot(words[5] + words[6])
                else:
                    bots[words[5] + words[6]] = Output(words[5] + words[6])
                bot.low = words[5] + words[6]
            if words[10] + words[11] in bots:
                if words[10] == "bot":
                    bot.high = words[10] + words[11]
            else:
                if words[10] == "bot":
                    bots[words[10] + words[11]] = Bot(words[10] + words[11])
                else:
                    bots[words[10] + words[11]] = Output(words[10] + words[11])
                bot.high = words[10] + words[11]
            bots[words[0] + words[1]] = bot
        else:
            if words[4] + words[5] in bots:
                bot = bots[words[4] + words[5]]
            else:
                bot = Bot(words[4] + words[5])
            bot.add_val(int(words[1]))
            bots[words[4] + words[5]] = bot
        for bot in bots:
            bots[bot].doaction()

    return answers


class Bot:
    def __init__(self, name):
        self.name = name
        self.vals = []
        self.low = ""
        self.high = ""

    def doaction(self):
        if len(self.vals) == 2 and self.low != "":
            self.vals.sort()
            if self.vals[0] == 17 and self.vals[1] == 61:
                answers["part1"] = self.name
            bots[self.high].add_val(self.vals.pop())
            bots[self.low].add_val(self.vals.pop())

    def add_val(self, val):
        if len(self.vals) < 2:
            self.vals.append(val)


class Output:
    def __init__(self, name):
        self.name = name
        self.vals = []

    def doaction(self):
        self.name = self.name

    def add_val(self, val):
        if self.name == "output0" or self.name == "output1" or self.name == "output2":
            answers["part2"] *= val
        self.vals.append(val)

print "Part1(): " + str(part1()["part1"])
print "Part1(): " + str(part1()["part2"])
