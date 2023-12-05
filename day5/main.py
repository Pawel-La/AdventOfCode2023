def task1(lines):
    n = len(lines)
    numbers = [int(x) for x in lines[0].split()[1:]]
    numbers_copy = [x for x in numbers]

    i = 1
    while i < n:
        if lines[i].split() and lines[i].split()[1] == "map:":
            i += 1

            while i < n and lines[i].split():
                [a, b, c] = [int(x) for x in lines[i].split()]

                for idx, number in enumerate(numbers):
                    if b <= number < b + c:
                        numbers_copy[idx] = a + number - b

                i += 1

            numbers = [x for x in numbers_copy]

        i += 1
    return min(numbers)


def task2(lines):
    nums = [int(x) for x in lines[0].split()[1:]]
    numbers = set([(nums[i], nums[i] + nums[i + 1] - 1, False) for i in
                   range(0, len(nums), 2)])

    n = len(lines)

    i = 1
    while i < n:
        if lines[i].split() and lines[i].split()[1] == "map:":
            i += 1

            list_of_numbers = [(x, y, False) for (x, y, _) in list(numbers)]
            numbers = set(list_of_numbers)

            while i < n and lines[i].split():
                [a, b, c] = [int(x) for x in lines[i].split()]

                for (from_n, to_n, used) in list(numbers):
                    if used or from_n >= b + c or to_n < b:
                        continue

                    numbers.remove((from_n, to_n, False))

                    if b <= from_n and to_n < b + c:
                        numbers.add((from_n + a - b, to_n + a - b, True))
                    elif b <= from_n and b + c <= to_n:
                        numbers.add((from_n + a - b, a + c - 1, True))
                        numbers.add((b + c, to_n, False))
                    elif from_n < b and to_n < b + c:
                        numbers.add((from_n, b - 1, False))
                        numbers.add((a, to_n + a - b, True))
                    elif from_n < b and b + c <= to_n:
                        numbers.add((from_n, b - 1, False))
                        numbers.add((a, a + c - 1, True))
                        numbers.add((b + c, to_n, False))

                i += 1
        i += 1

    return min([x for (x, y, z) in numbers])


def read_input():
    with open('day5/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    task1(lines)
    print(task2(lines))
