import md5

input = "ugkcyxxp"


def part1():
    x = 0
    pwd = ""
    print '{:_<8}'.format(pwd)
    while True:
        m = md5.new()
        m.update(input)
        m.update(str(x))
        digest = m.hexdigest()
        if digest.startswith("00000"):
            pwd += digest[5:6]
            print '{:_<8}'.format(pwd)
        x += 1
        if len(pwd) == 8:
            break
    return pwd


def part2():
    x = 0
    pwd = list("_" * 8)
    print "".join(pwd)
    while True:
        m = md5.new()
        m.update(input)
        m.update(str(x))
        digest = m.hexdigest()
        if digest.startswith("00000"):
            loc = ord(digest[5:6])
            if 48 <= loc <= 55 and pwd[int(chr(loc))] == "_":
                pwd[int(chr(loc))] = digest[6:7]
                print "".join(pwd)
        x += 1
        if "_" not in pwd:
            break
    return "".join(pwd)


print "Part1: " + str(part1())
print "Part2: " + str(part2())
