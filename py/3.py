off_lower = ord("a") - 1
off_upper = ord("A") - 1 - 26


def sum_of(s: str) -> dict:
    n = 0
    for c in s:
        if c.upper() == c:
            n += ord(c) - off_upper
        else:
            n += ord(c) - off_lower
    return n


def part_a(filename):
    s = ""
    with open(filename) as f:
        for line in f:
            line = line.strip()
            l = len(line) // 2
            for c in line[:l]:
                if c in line[l:]:
                    s += c
                    break
    return sum_of(s)


def part_b(filename):
    s = ""
    with open(filename) as f:
        lines = f.readlines()

    i = 0
    inc = 3
    while i < len(lines):
        three_elves = lines[i : i + inc]
        for c in three_elves[0]:
            if c in three_elves[1] and c in three_elves[2]:
                s += c
                break
        i += inc
    return sum_of(s)


if __name__ == "__main__":
    ex = "examples/3.txt"
    f = "build/3"
    assert part_a(ex) == 157
    print(part_a(f))
    assert part_b(ex) == 70
    print(part_b(f))
