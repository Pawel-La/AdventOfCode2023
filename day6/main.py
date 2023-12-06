def task1(lines):
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    races = [(times[i], distances[i]) for i in range(len(times))]

    result = 1
    for (time, distance) in races:
        for i in range(time):
            if i * (time - i) > distance:
                start = i

        for i in range(time, -1, -1):
            if i * (time - i) > distance:
                end = i

        number_of_ways = start - end + 1
        result *= number_of_ways

    return result


def task2(lines):
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    time = int(''.join(times))
    distance = int(''.join(distances))

    for i in range(time):
        if i * (time - i) > distance:
            start = i
            break

    for i in range(time, -1, -1):
        if i * (time - i) > distance:
            end = i
            break

    return end - start + 1


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    task1(lines)
    print(task2(lines))
