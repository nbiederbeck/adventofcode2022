from copy import copy


def parse(filename):
    return list(map(int, open(filename).readlines()))


def part_a(numbers):
    l = len(numbers)
    before = copy(numbers)

    # "sorting"
    for n in before:
        idx = numbers.index(n)
        numbers.remove(n)

        idx += n
        idx = idx % len(numbers)

        if idx == 0:
            numbers.append(n)
        else:
            numbers.insert(idx, n)

    # find after 0
    idx = numbers.index(0)
    nums = list(numbers[(idx + i) % l] for i in (1000, 2000, 3000))
    return sum(nums)


if __name__ == "__main__":
    ex = parse("examples/20.txt")
    f = parse("build/20")
    assert part_a(ex) == 3
    print(part_a(f))
