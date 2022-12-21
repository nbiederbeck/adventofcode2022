from operator import add, floordiv, mul, sub


def parse(input):
    d = {}
    for line in input:
        result, expression = map(str.strip, line.strip().split(":"))
        try:
            expression = int(expression)
        except ValueError:
            pass
        d[result.strip()] = expression
    return d


ops = {"+": add, "-": sub, "*": mul, "/": floordiv}


def evaluate(res, exp, args):
    if isinstance(exp, int):
        return exp

    a, op, b = exp.split()
    op = ops[op]

    a = evaluate(a, args[a], args)
    b = evaluate(b, args[b], args)

    return op(a, b)


def part_a(input):
    return evaluate("root", input["root"], input)


if __name__ == "__main__":
    ex = parse(open("examples/21.txt").readlines())
    assert part_a(ex) == 152
    f = parse(open("build/21").readlines())
    print(part_a(f))
