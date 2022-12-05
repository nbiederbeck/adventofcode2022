def stacks_from_crates(crates):
    crates = crates.split("\n")
    crate_numbers = crates[-1]
    n_stacks = int(crate_numbers.replace(" ", "")[-1])
    stacks = []
    for i in range(n_stacks):
        num = i * 4 + 1
        stack = []
        for line in crates[:-1]:
            if len(line) > num:
                if line[num] != " ":
                    stack.append(line[num])
        stacks.append(stack[::-1])
    return stacks


def test_stacks_from_crates():
    assert stacks_from_crates("[A]\n 1") == [["A"]]
    assert stacks_from_crates("[A] [B]\n 1  2") == [["A"], ["B"]]
    assert stacks_from_crates("[A]\n[B]\n 1") == [["B", "A"]]
    assert stacks_from_crates("    [A]\n    [B]\n 1  2") == [[], ["B", "A"]]


test_stacks_from_crates()


def parse_input(filename):
    with open(filename) as f:
        puzzle = f.read()
    crates, moves = puzzle.split("\n\n")
    moves = [_ for _ in moves.split("\n")]
    stacks = stacks_from_crates(crates)
    return stacks, moves


def move(crates, instruction):
    _, count, _, start, _, stop = instruction.split(" ")
    count = int(count)
    start = int(start) - 1
    stop = int(stop) - 1
    for _ in range(count):
        crates[stop].append(crates[start].pop())
    return crates


def part_a(filename):
    crates, moves = parse_input(filename)
    for ins in moves[:-1]:
        crates = move(crates, ins)
    first = ""
    for c in crates:
        if c[-1] != "":
            first += c[-1]
    return first


def move_b(crates, instruction):
    _, count, _, start, _, stop = instruction.split(" ")
    count = int(count)
    start = int(start) - 1
    stop = int(stop) - 1
    crates[stop].extend(crates[start][-count:])
    crates[start] = crates[start][:-count]
    return crates


def part_b(filename):
    crates, moves = parse_input(filename)
    for ins in moves[:-1]:
        crates = move_b(crates, ins)
    first = ""
    for c in crates:
        if c[-1] != "":
            first += c[-1]
    return first


if __name__ == "__main__":
    ex = "examples/5.txt"
    f = "build/5"
    assert part_a(ex) == "CMZ"
    print(part_a(f))
    assert part_b(ex) == "MCD"
    print(part_b(f))
