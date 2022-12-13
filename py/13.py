def parse(f):
    return [list(map(eval, d.split("\n"))) for d in open(f).read()[:-1].split("\n\n")]


def check(left: list, right: list):
    for x, y in zip(left, right):
        if isinstance(x, (int)) and isinstance(y, (int)):
            # int, int
            if x < y:
                return True
            elif x > y:
                return False
            else:
                continue
        elif isinstance(x, (int)) and not isinstance(y, (int)):
            c = check([x], y)
            if c is None:
                continue
            else:
                return c
        elif not isinstance(x, (int)) and isinstance(y, (int)):
            c = check(x, [y])
            if c is None:
                continue
            else:
                return c
        else:
            # list, list
            c = check(x, y)
            if c is None:
                continue
            else:
                return c

    # no decision
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return None


def part_a(input):
    indices_right_order = []
    for index, (left, right) in enumerate(input):
        if check(left, right):
            indices_right_order.append(index + 1)

    return sum(indices_right_order)


if __name__ == "__main__":
    ex = parse("examples/13.txt")
    assert part_a(ex) == 13
    f = parse("build/13")
    print(part_a(f))
