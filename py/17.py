def create_rock(height: int, shape: int):
    shape %= 5
    h = height + 4
    if shape == 0:
        rock = {(2, h), (3, h), (4, h), (5, h)}
    elif shape == 1:
        rock = {(2, h + 1), (3, h + 1), (4, h + 1), (3, h), (3, h + 2)}
    elif shape == 2:
        rock = {(2, h), (3, h), (4, h), (4, h + 1), (4, h + 2)}
    elif shape == 3:
        rock = {(2, h), (2, h + 1), (2, h + 2), (2, h + 3)}
    elif shape == 4:
        rock = {(2, h), (3, h), (2, h + 1), (3, h + 1)}
    return rock


def move(rock, direction, chamber):
    if direction == "<":
        r = {(x - 1, y) for (x, y) in rock}
    elif direction == ">":
        r = {(x + 1, y) for (x, y) in rock}
    else:
        raise ValueError(f"{direction=} not supported")

    if is_inside(r) and no_hit(r, chamber):
        return r
    return rock


def no_hit(rock, chamber):
    return len(chamber & rock) == 0


def fall(rock):
    return {(x, y - 1) for (x, y) in rock}


def can_fall(rock, chamber):
    return len(chamber & fall(rock)) == 0


def is_inside(rock):
    for (x, y) in rock:
        if x < 0 or x > 6:
            return False
    return True


def max_height(chamber):
    return max(y for (x, y) in chamber)


def print_chamber(chamber):
    for y in range(1, max_height(chamber) + 1)[::-1]:
        print("|", end="")
        for x in range(7):
            if (x, y) in chamber:
                print("#", end="")
            else:
                print(".", end="")
        print("|")
    print("+-------+")


def part_a(jets):
    chamber = {(i, 0) for i in range(7)}

    d = 0
    for r in range(2022):

        rock = create_rock(max_height(chamber), r)

        while True:
            direction = jets[d % len(jets)]

            rock = move(rock, direction, chamber)
            d += 1

            if can_fall(rock, chamber):
                rock = fall(rock)
            else:
                break

        chamber |= rock

    return max_height(chamber)


if __name__ == "__main__":
    ex = open("examples/17.txt").read().strip()
    assert part_a(ex) == 3068
    f = open("build/17").read().strip()
    print(part_a(f))
