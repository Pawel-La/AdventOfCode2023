import math


def get_number_of_ways(time, distance):
    number_of_ways = 1
    for i in range(time):
        if i * (time - i) > distance:
            number_of_ways -= i
            break

    for i in range(time, -1, -1):
        if i * (time - i) > distance:
            number_of_ways += i
            break

    return number_of_ways


def task1(lines):
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    return math.prod(get_number_of_ways(time, distance)
                     for (time, distance) in zip(times, distances))


def task2(lines):
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))
    return get_number_of_ways(time, distance)


def read_input():
    with open('../day6/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    print(task1(lines))
    print(task2(lines))
