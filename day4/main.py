def get_count(line):
    tab = list(filter(lambda a: a.isdigit() or a == "|", line.split(" ")))
    idx = tab.index("|")
    return sum([1 if number in tab[:idx] else 0 for number in tab[idx + 1:]])


def task1(lines):
    return sum([int(pow(2, get_count(line) - 1)) for line in lines])


def task2(lines):
    cache = {i: 1 for i in range(1, len(lines) + 1)}

    for i, line in enumerate(lines, 1):
        for j in range(i+1, i+1+get_count(line)):
            cache[j] += cache[i]

    return sum(cache.values())


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    print(task1(lines))
    print(task2(lines))
