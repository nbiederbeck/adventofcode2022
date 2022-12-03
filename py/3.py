result = {"a": 157, "b": 70}

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
    assert part_a("examples/3.txt") == result["a"]
    print(part_a("build/3"))
    assert part_b("examples/3.txt") == result["b"]
    print(part_b("build/3"))
