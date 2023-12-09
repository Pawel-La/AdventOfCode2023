import re


def get_dirs_and_d(lines):
    d = {}
    dirs = ""

    for i, line in enumerate(lines):
        if i == 0:
            dirs = [0 if c == "L" else 1 for c in line]
        if i >= 2:
            [a, b, c] = re.findall(r'\w+', line)
            d[a] = (b, c)
    return dirs, d


def task1(lines):
    dirs, d = get_dirs_and_d(lines)

    word = "AAA"
    steps = 0

    while word != "ZZZ":
        dir = dirs[steps % len(dirs)]
        word = d[word][dir]
        steps += 1

    return steps


def get_cycle_dpp(d, dirs, ops=100_000):
    cycle_d = {}
    for org_word in d.keys():
        word = org_word
        for dir in dirs:
            word = d[word][dir]
        cycle_d[org_word] = word

    cycle_dpp = {}
    for org_word in cycle_d.keys():
        t = []
        word = org_word
        for i in range(ops):
            if word[-1] == "Z":
                t.append(i)
            word = cycle_d[word]
        cycle_dpp[org_word] = (word, set(t))
    return cycle_dpp


def task2(lines):
    ops = 50_000
    dirs, d = get_dirs_and_d(lines)
    cycle_dpp = get_cycle_dpp(d, dirs, ops)

    words = list(filter(lambda key: key[-1] == "A", d.keys()))

    steps = 0
    while 1:
        info = [cycle_dpp[word] for word in words]
        if set.intersection(*map(set, [i[1] for i in info])):
            break
        words = [i[0] for i in info]
        steps += len(dirs) * ops

    a = set.intersection(*map(set, [cycle_dpp[word][1] for word in words]))
    return steps + min(list(a)) * len(dirs)


def read_input():
    with open('../day8/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    print(task1(lines))
    print(task2(lines))
