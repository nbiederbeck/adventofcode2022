def inc(c, x, stop, signals):
    if c in stop:
        signals.append(c * x)
    return signals


def draw(c, x, screen, w=40):
    c -= 1
    sprite = [x - 1, x, x + 1]

    if c % 40 in sprite:
        screen[c] = "#"
    return screen


def pprint(s, w=40):
    print("\n".join(["".join(s[w * i : w * i + w]) for i in range(len(s) // w)]))


def part(filename):
    stop = [20, 60, 100, 140, 180, 220]
    c = 1
    x = 1
    signals = []
    screen = ["." for _ in range(240)]
    for line in open(filename).readlines():
        line = line.strip()
        if line == "noop":
            # at the start
            # during the cycle
            screen = draw(c, x, screen)
            signals = inc(c, x, stop, signals)
            # after the cycle
            c += 1
        else:
            assert line.startswith("addx")
            v = int(line.split(" ")[1])
            # at the start
            # during the first cycle
            signals = inc(c, x, stop, signals)
            screen = draw(c, x, screen)
            # after first cycle
            c += 1
            # during the second cycle
            screen = draw(c, x, screen)
            signals = inc(c, x, stop, signals)
            # after second cycle
            c += 1
            x += v
    return sum(signals), screen


if __name__ == "__main__":
    f = "build/10"
    ex = "examples/10.txt"
    assert part(ex), _ == (13140, _)
    print(part(f)[0])
    # pprint(part(ex)[1])  # visually assert correctness
    pprint(part(f)[1])
