def get_with_board(input):
    n = len(input[0])
    m = len(input)
    with_board = [["." for _ in range(n + 2)] for _ in range(m + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            with_board[i][j] = input[i - 1][j - 1]
    return with_board


def task1(input):
    def is_part(field):
        return not field.isdigit() and field != "."

    def is_part_number(a, b):
        for c in range(a - 1, a + 2):
            if is_part(with_board[c][b]):
                return True
        return False

    n = len(input[0])
    m = len(input)
    with_board = get_with_board(input)
    result = 0

    for i in range(1, n+2):
        j = 1
        while j < m + 2:
            if with_board[i][j].isdigit():
                part_number = is_part_number(i, j - 1) or \
                              is_part_number(i, j)

                number = int(with_board[i][j])
                j += 1
                while with_board[i][j].isdigit():
                    number *= 10
                    number += int(with_board[i][j])
                    part_number = part_number or is_part_number(i, j)
                    j += 1

                part_number = part_number or is_part_number(i, j)

                if part_number:
                    result += number
            else:
                j += 1

    return result


def task2(input):
    def get_new_gears(a, b):
        new_gears = []
        for c in range(a - 1, a + 2):
            if with_board[c][b] == "*":
                new_gears.append((c, b))
        return new_gears

    n = len(input[0])
    m = len(input)
    with_board = get_with_board(input)
    potential = {}

    for i in range(1, n + 2):
        j = 1
        while j < m + 2:
            gears = []

            if with_board[i][j].isdigit():
                gears.extend(get_new_gears(i, j - 1))
                gears.extend(get_new_gears(i, j))

                number = int(with_board[i][j])
                j += 1
                while with_board[i][j].isdigit():
                    number *= 10
                    number += int(with_board[i][j])
                    gears.extend(get_new_gears(i, j))
                    j += 1

                gears.extend(get_new_gears(i, j))

                for gear in gears:
                    if gear not in potential:
                        potential[gear] = []
                    potential[gear].append(number)

            else:
                j += 1

    return sum([x[0] * x[1] if len(x) == 2 else 0 for x in potential.values()])


def read_input():
    with open('../day3/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    input = read_input()
    print(task1(input))
    print(task2(input))
