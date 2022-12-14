from collections import defaultdict
from copy import copy


def split(s, where=","):
    return s.split(where)


def fill_between(edges):
    cave = defaultdict(dict)

    for i in range(len(edges) - 1):
        start = tuple(map(int, edges[i]))
        stop = tuple(map(int, edges[i + 1]))
        dx = stop[0] - start[0]
        dy = stop[1] - start[1]
        if dx == 0:
            x = start[0]
            if dy < 0:
                ys = {y: "#" for y in range(stop[1], start[1] + 1)}
            else:
                ys = {y: "#" for y in range(start[1], stop[1] + 1)}
            cave[x] |= ys
        elif dy == 0:
            y = start[1]
            ys = {y: "#"}
            if dx < 0:
                xs = range(stop[0], start[0] + 1)
            else:
                xs = range(start[0], stop[0] + 1)
            for x in xs:
                cave[x] |= ys

    return cave


def print_cave(cave):
    min_x = min(cave.keys())
    min_y = min([y for v in cave.values() for y in v.keys()])
    max_x = max(cave.keys())
    max_y = max([y for v in cave.values() for y in v.keys()])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            c = cave.get(x)
            if c is not None:
                c = c.get(y, ".")
            else:
                c = "."
            print(c, end="")
        print()


def parse(filename):
    cave = defaultdict(dict)
    for line in open(filename).readlines():
        edges = list(map(split, map(str.strip, line.split("->"))))
        for x, ys in fill_between(edges).items():
            cave[x] |= ys
    return cave


def part_a(cave, b=False):
    init_sand = {"x": 500, "y": 0}
    n_sand = 0
    max_y = max([y for v in cave.values() for y in v.keys()])

    sand = copy(init_sand)
    while True:
        # drop down
        x = sand["x"]
        y = sand["y"] + 1

        if y > max_y:
            # fall into abyss
            break

        if y not in cave[x]:
            sand["y"] = y

        # drop down and left
        elif y not in cave[x - 1]:
            sand["y"] = y
            sand["x"] -= 1

        # drop down and right
        elif y not in cave[x + 1]:
            sand["y"] = y
            sand["x"] += 1

        else:
            # sand is at rest
            cave[sand["x"]][sand["y"]] = "o"
            sand = copy(init_sand)
            n_sand += 1

    print_cave(cave)
    return n_sand


if __name__ == "__main__":
    ex = parse("examples/14.txt")
    f = parse("build/14")
    assert part_a(copy(ex)) == 24
    print(part_a(copy(f)))
    # assert part_a(copy(ex), b=True) == 93
    # print(part_a(copy(f), b=True))
