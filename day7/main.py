def task1(lines):
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    decks = []
    for line in lines:
        [a, b] = line.split()
        bid = int(b)
        cards = [c for c in a]
        rank = sorted([cards.count(card) for card in cards])[::-1]
        decks.append((rank, [values[card] for card in cards], bid))

    return sum([(i+1) * z for i, (x,y,z) in enumerate(sorted(decks))])


def simplify(card_counts):
    x = sorted(card_counts)
    result = []
    i = 0
    while i < len(x):
        result.append(x[i])
        i += x[i]
    return sorted(result)


def get_rank(cards):
    jokers = sum(1 if i == "J" else 0 for i in cards)
    cards_without_jokers = list(filter(lambda card: card != "J", cards))
    res = [0, 0]
    x = [cards_without_jokers.count(card) for card in cards_without_jokers]
    res.extend(simplify(x))

    best, second_best = res[-1] + jokers, res[-2]
    return best, second_best


def task2(lines):
    values = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
              "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}

    decks = []
    for line in lines:
        [a, b] = line.split()
        bid = int(b)
        cards = [c for c in a]
        rank = get_rank(cards)
        decks.append((rank, [values[card] for card in cards], bid))

    return sum([(i + 1) * z for i, (x, y, z) in enumerate(sorted(decks))])


def read_input():
    with open('../day7/input.txt', 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    lines = read_input()
    print(task1(lines))
    print(task2(lines))
