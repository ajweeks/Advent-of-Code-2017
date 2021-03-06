
def get_input():
    return [int(x.replace('\n', '')) for x in open("day01.in").readlines()]


def part1():
    lines = get_input()
    s = sum([int(x / 3 - 2) for x in lines])
    return s


def part2():
    lines = get_input()
    s = 0
    for x in lines:
        xs = x
        while xs > 0:
            xs = int(xs / 3 - 2)
            if xs > 0:
                s += xs
    return s
