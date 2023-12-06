def task1(i):
    import re
    g = lambda a, b, c: all(int(x) <= b for x in re.findall(fr'(\d+) {a}', c))

    return sum([i for i, l in enumerate(i, 1)
                if g("r", 12, l) and
                g("g", 13, l) and
                g("b", 14, l)])


def task2(i):
    import re
    g = lambda a, c: max(int(x) for x in re.findall(fr'(\d+) {a}', c))

    return sum([g("r", l) * g("g", l) * g("b", l) for l in i])


def read_input():
    with open('../day2/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    print(task1(lines))
    print(task2(lines))
