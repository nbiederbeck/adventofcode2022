def range_to_set(rng):
    a, b = map(int, rng.split("-"))
    return set(range(a, b + 1))


def test_range_to_set():
    assert range_to_set("2-4") == {2, 3, 4}


test_range_to_set()


def parse_line_into_sets(line):
    a, b = map(range_to_set, line.split(","))
    return a, b


def test_parse_line_into_sets():
    line = "2-4,6-8"
    a, b = parse_line_into_sets(line)
    assert a == {2, 3, 4}
    assert b == {6, 7, 8}


test_parse_line_into_sets()


def run(filename, comparison):
    inc = 0
    with open(filename) as f:
        for line in f.readlines():
            a, b = parse_line_into_sets(line.strip())
            if comparison(a, b):
                inc += 1
    return inc


def part_a(filename):
    def issubset(a, b):
        return a <= b or b <= a

    return run(filename, issubset)


def part_b(filename):
    def intersection_notempty(a, b):
        return len(a & b) > 0

    return run(filename, intersection_notempty)


if __name__ == "__main__":
    ex = "examples/4.txt"
    f = "build/4"
    assert part_a(ex) == 2
    print(part_a(f))
    assert part_b(ex) == 4
    print(part_b(f))
