from operator import add, mul, pow


def parse_operation(operation):
    op = operation.split("= ")[1]
    _, operator, argument = op.split(" ")

    if argument == "old":
        operator = pow
        argument = 2
    else:
        if operator == "*":
            operator = mul
        elif operator == "+":
            operator = add
        else:
            raise ValueError("Could not parse operation.")
        argument = int(argument)

    def f(value):
        return operator(value, argument)

    return f


def parse_input(filename):
    monkey_input = open(filename).read().split("\n\n")

    monkeys = {}

    for i, mon in enumerate(monkey_input):

        # don't know why this parsing is so dumb ...
        mon = mon.split("\n")
        if mon[-1] == "":
            mon = mon[:-1]
        assert len(mon) == 6, mon

        monkeys[i] = {
            "items": list(map(int, mon[1].split(":")[1].split(","))),
            "operation": parse_operation(mon[2]),
            "test": int(mon[3].split(" ")[-1]),
            True: int(mon[4][-1]),
            False: int(mon[5][-1]),
            "inspections": 0,
        }

    return monkeys


def test_and_how_to():
    monkeys = parse_input("examples/11.txt")
    assert monkeys[0]["items"] == [79, 98]
    assert monkeys[2]["operation"](20) == 400
    assert 34 % monkeys[3]["test"] == 0
    assert not 20 % monkeys[1]["test"] == 0
    assert monkeys[1][True] == 2
    assert monkeys[0][False] == 3


def part(filename, level, rounds):
    monkeys = parse_input(filename)

    primes = 1
    for m in monkeys.values():
        primes *= m["test"]

    for r in range(rounds):
        for i in range(len(monkeys)):
            m = monkeys[i]

            n_items = len(m["items"])
            m["inspections"] += n_items

            for _ in range(n_items):
                # inspect item (increases worry)
                item = m["items"].pop(0)
                worry = m["operation"](item)
                # relief (divide by 3, round down)
                worry = worry // level
                # test worry level (test)
                throw_to = m[worry % m["test"] == 0]
                # throw away
                monkeys[throw_to]["items"].append(worry % primes)

    ins = list(reversed(sorted([m["inspections"] for m in monkeys.values()])))
    return ins[0] * ins[1]


if __name__ == "__main__":
    ex = "examples/11.txt"
    f = "build/11"
    test_and_how_to()

    args = {"level": 3, "rounds": 20}
    assert part(ex, **args) == 10605
    print(part(f, **args))

    args = {"level": 1, "rounds": 10000}
    assert part(ex, **args) == 2713310158
    print(part(f, **args))
