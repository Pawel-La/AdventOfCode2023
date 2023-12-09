import re


def task1(lines):
    d = {}
    dirs = ""

    for i, line in enumerate(lines):
        if i == 0:
            dirs = [0 if c == "L" else 1 for c in line]
        if i >= 2:
            [a, b, c] = re.findall(r'\w+', line)
            d[a] = (b, c)

    word = "AAA"
    steps = 0

    while word != "ZZZ":
        dir = dirs[steps % len(dirs)]
        word = d[word][dir]
        steps += 1

    return steps


def task2(lines):
    d = {}
    dirs = ""

    for i, line in enumerate(lines):
        if i == 0:
            dirs = [0 if c == "L" else 1 for c in line]
        if i >= 2:
            [a, b, c] = re.findall(r'\w+', line)
            d[a] = (b, c)

    words = list(filter(lambda key: key[-1] == "A", d.keys()))
    print(words)
    # steps = 0
    #
    # while word != "ZZZ":
    #     dir = dirs[steps % len(dirs)]
    #     word = d[word][dir]
    #     steps += 1

    # return steps


def read_input():
    with open('../day8/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    # print(task1(lines))
    task2(lines)
    # print([0 if x == "a" else 1 for x in "abc"])