class Tree:
    def __init__(self, name, size=None, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = children or {}
        self._size = size or None

    def add_child(self, tree):
        tree.parent = self
        self.children[tree.name] = tree
        return tree

    def __str__(self) -> str:
        level = ""
        tree = self
        while tree.parent is not None:
            tree = tree.parent
            level += "  "

        return f"- {self.name} {self.size_str}\n" + "".join(
            f"  {level}{child}" for child in self.children.values()
        )

    @property
    def size_str(self) -> str:
        if self._size is None:
            return "(dir)"
        return f"(file, size={self._size})"

    @property
    def size(self) -> int:
        if self._size is None:
            return sum(child.size for child in self.children.values())
        return self._size

    def walkdirs(self):
        if len(self.children) == 0:
            return []
        full = [self]
        for child in self.children.values():
            full.extend(child.walkdirs())
        return full

    def small(self):
        total = 0
        for d in self.walkdirs():
            s = d.size
            if s < 100000:
                total += s
        return total

    def delete(self):
        total = 70000000
        required = 30000000
        possibles = []
        for d in self.walkdirs():
            if total - self.size + d.size > required:
                possibles.append(d.size)
        return min(possibles)


def parse(text):
    text = text.split("\n")
    assert "/" in text[0], "Must start parsing at root."
    tree = Tree("/")
    for line in text[1:-1]:
        if line.startswith("$ cd"):
            *_, target = line.split(" ")
            if target == "..":
                tree = tree.parent
            else:
                tree = tree.children[target]
        elif line == "$ ls":
            pass
        else:  # command must be ls
            size, name = line.split(" ")
            if size == "dir":
                tree.add_child(Tree(name))
            else:
                tree.add_child(Tree(name, int(size)))

    while tree.parent is not None:
        tree = tree.parent

    return tree


if __name__ == "__main__":
    example = open("examples/7.txt").read()
    example_input = open("examples/7_example.txt").read()

    tree = parse(example)

    assert str(tree) == example_input
    assert tree.size == 48381165
    assert tree.small() == 95437  # a
    assert tree.delete() == 24933642  # b

    tree = parse(open("build/7").read())
    print(tree.small())
    print(tree.delete())
