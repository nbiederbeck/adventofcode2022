from copy import copy


def parse(filename):
    return list(map(int, open(filename).readlines()))


def part_a(numbers):
    l = len(numbers)
    before = copy(numbers)

    print(numbers)
    for i, n in enumerate(before):
        idx = (i + n) % l
        numbers.remove(n)
        numbers.insert(idx, n)

        print(numbers)


if __name__ == "__main__":
    ex = parse("examples/20.txt")
    f = parse("build/20")
    assert part_a(ex) == 3
    print(part_a(f))
