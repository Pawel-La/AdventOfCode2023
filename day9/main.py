def get_next_value(values):
    next_value = 0
    while not all([True if x == 0 else False for x in values]):
        next_value += values[-1]
        values = [values[i+1] - values[i] for i in range(len(values) - 1)]
    return next_value


def task1(lines):
    return sum(get_next_value([int(x) for x in line.split()]) for line in lines)


def get_prev_value(values):
    prev_value = 0
    sign_count = 0

    while not all([True if x == 0 else False for x in values]):
        prev_value += values[0] * pow(-1, sign_count)
        sign_count += 1
        values = [values[i+1] - values[i] for i in range(len(values) - 1)]
    return prev_value


def task2(lines):
    return sum(get_prev_value([int(x) for x in line.split()]) for line in lines)


def read_input():
    with open('../day9/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    print(task1(lines))
    print(task2(lines))
