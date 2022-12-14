from ast import literal_eval
from functools import cmp_to_key


def parse(f):
    return [
        list(map(literal_eval, d.split("\n")))
        for d in open(f).read()[:-1].split("\n\n")
    ]


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


def wrap_check(*tup):
    c = check(*tup)
    if c is True:
        return -1
    if c is False:
        return 1
    return 0


def part_b(input):
    div_a = [[2]]
    div_b = [[6]]
    lists = [div_a, div_b]
    for left, right in input:
        lists.append(left)
        lists.append(right)

    sort = sorted(lists, key=cmp_to_key(wrap_check))
    return (sort.index(div_a) + 1) * (sort.index(div_b) + 1)


if __name__ == "__main__":
    ex = parse("examples/13.txt")
    f = parse("build/13")
    assert part_a(ex) == 13
    print(part_a(f))
    assert part_b(ex) == 140
    print(part_b(f))
