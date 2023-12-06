def task1(y):
    f = lambda l: list(filter(lambda x: x.isdigit(), l))
    return sum(int(f(l)[0] + f(l)[-1]) for l in y)


def task2(i):
    import re

    def g(l):
        n = ["one", "two", "three", "four", "five", "six", "seven", "eight",
             "nine"]
        x = re.findall(f'(?=(\d|{"|".join(n)}))', l)

        f = lambda a: str(n.index(a) + 1) if a in n else a

        return int(f(x[0]) + f(x[-1]))

    return sum(g(o) for o in i)


def read_input():
    with open('../day1/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    task1(lines)
    task2(lines)
