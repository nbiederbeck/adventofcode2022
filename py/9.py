def visualize(knots):
    xs = [k[0] for k in knots]
    ys = [k[1] for k in knots]

    x_max = max(xs)
    x_min = min(xs)
    y_max = max(ys)
    y_min = min(ys)

    grid = [["." for _ in range(1 + x_max - x_min)] for _ in range(1 + y_max - y_min)]

    for x, y in knots:
        grid[y][x] = "#"

    grid = ["".join(line) for line in grid[::-1]]
    print("\n".join(grid))


def move_head(head, d):
    assert d in "RLUD"
    x, y = head
    if d == "R":
        x += 1
    elif d == "L":
        x -= 1
    elif d == "U":
        y += 1
    elif d == "D":
        y -= 1
    return x, y


def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail

    if (abs(hx - tx) <= 1) and (abs(hy - ty) <= 1):
        return tail

    if (hx - tx) >= 1:
        tx += 1
    elif (hx - tx) <= -1:
        tx -= 1

    if (hy - ty) >= 1:
        ty += 1
    elif (hy - ty) <= -1:
        ty -= 1

    return tx, ty


def test_move_head():
    head = (1, 0)
    assert move_head(head, "R") == (2, 0)


def test_move_diagonally():
    head = (4, 1)
    tail = (3, 0)
    assert move_tail(head, tail) == tail

    head = (4, 2)
    assert move_tail(head, tail) == (4, 1)


def part_a(filename):
    moves = open(filename).readlines()
    head = tail = (0, 0)
    visited = [tail]
    for move in moves:
        direction, count = move.split(" ")
        count = int(count)
        for _ in range(count):
            head = move_head(head, direction)
            tail = move_tail(head, tail)
            visited.append(tail)

    return len(set(visited))


def part_b(filename):
    moves = open(filename).readlines()
    knots = [(0, 0) for _ in range(10)]
    visited = [(0, 0)]
    for move in moves:
        direction, count = move.split(" ")
        count = int(count)
        for _ in range(count):
            knots[0] = move_head(knots[0], direction)
            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i - 1], knots[i])
            visited.append(knots[-1])

    return len(set(visited))


if __name__ == "__main__":
    ex = "examples/9.txt"
    f = "build/9"
    test_move_head()
    test_move_diagonally()
    assert part_a(ex) == 13
    print(part_a(f))

    assert part_b(ex) == 1
    assert part_b("examples/9_2.txt") == 36
    print(part_b(f))
