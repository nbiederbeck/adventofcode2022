from tqdm import tqdm


def manhatten(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def parse_positions(s):
    x, y = s.split(",")
    x = int(x.split("=")[1])
    y = int(y.split("=")[1])
    return x, y


def parse(filename):
    sensors = []

    for line in open(filename).readlines():
        s, b = line.split(":")

        x, y = parse_positions(s)
        bx, by = parse_positions(b)

        sensor = {
            "x": x,
            "y": y,
            "bx": bx,
            "by": by,
            "d": manhatten(x, bx, y, by),
        }
        sensors.append(sensor)

    return sensors


def part_a(sensors, y=2000000):
    occupied = set()
    for s in sensors:
        dy = abs(y - s["y"])
        dx = s["d"] - dy
        if dx > 0:
            for x in range(s["x"] - dx, s["x"] + dx + 1):
                if not (x == s["bx"] and y == s["by"]):
                    occupied |= {x}
    return occupied


if __name__ == "__main__":
    ex = parse("examples/15.txt")
    assert len(part_a(ex, y=10)) == 26
    f = parse("build/15")
    print(len(part_a(f)))
