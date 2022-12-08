def get_row(row, trees):
    return trees[row]


def get_col(col, trees):
    return "".join(row[col] for row in trees)


def part_a(filename):
    trees = open(filename).read()[:-1]  # skip last newline
    trees = trees.split("\n")
    n_rows = len(trees)
    n_cols = len(trees[0])

    total = 2 * n_rows + 2 * n_cols - 4
    min_row, max_row = 1, n_rows - 1
    min_col, max_col = 1, n_cols - 1

    for i in range(min_row, max_row):
        for j in range(min_col, max_col):
            tree = trees[i][j]
            row = get_row(i, trees)
            col = get_col(j, trees)
            if (
                all(t < tree for t in row[:j])
                or all(t < tree for t in row[j + 1 :])
                or all(t < tree for t in col[:i])
                or all(t < tree for t in col[i + 1 :])
            ):
                total += 1
    return total


def part_b(filename):

    trees = open("examples/8.txt").read()[:-1].split("\n")
    a = scenic_score(trees[1][2], get_row(1, trees), get_col(2, trees), 1, 2)
    assert a == 4
    b = scenic_score(trees[3][2], get_row(3, trees), get_col(2, trees), 3, 2)
    assert b == 8

    trees = open(filename).read()[:-1].split("\n")

    n_rows = len(trees)
    n_cols = len(trees[0])

    min_row, max_row = 1, n_rows - 1
    min_col, max_col = 1, n_cols - 1

    min_row, max_row = 0, n_rows
    min_col, max_col = 0, n_cols

    scores = []
    for i in range(min_row, max_row):
        for j in range(min_col, max_col):
            tree = trees[i][j]
            row = get_row(i, trees)
            col = get_col(j, trees)
            scores.append(scenic_score(tree, row, col, i, j))

    return max(scores)


def scenic_score(tree, row, col, i, j):

    left_of = 0
    for t in row[:j][::-1]:
        left_of += 1
        if t >= tree:
            break

    right_of = 0
    for t in row[j + 1 :]:
        right_of += 1
        if t >= tree:
            break

    top_of = 0
    for t in col[:i][::-1]:
        top_of += 1
        if t >= tree:
            break

    below_of = 0
    for t in col[i + 1 :]:
        below_of += 1
        if t >= tree:
            break

    return left_of * right_of * top_of * below_of


if __name__ == "__main__":
    ex = "examples/8.txt"
    f = "build/8"
    assert part_a(ex) == 21
    print(part_a(f))
    print(part_b(f))
