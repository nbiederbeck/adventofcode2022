def find_marker(s: str, w=4) -> int:
    for i in range(w, len(s)):
        window = s[i - w : i]
        if len(set(window)) == w:
            return i


def part_a(filename, w=4):
    puzzle = open(filename).read()
    chars_to_read = find_marker(puzzle, w)
    return chars_to_read


if __name__ == "__main__":
    ex = "examples/6.txt"
    f = "build/6"
    ex = open(ex).readlines()
    for sol, puz in zip([5, 6, 10, 11], ex):
        assert find_marker(puz) == sol
    print(part_a(f))
    for sol, puz in zip([23, 23, 29, 26], ex):
        assert find_marker(puz, w=14) == sol
    print(part_a(f, 14))
