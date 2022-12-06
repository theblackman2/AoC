import string

symbols = [letter for letter in string.ascii_letters]


def split_in_half(l: list) -> list:
    half = len(l) // 2
    return [list(l[:half]), list(l[half:])]


def slpit_list_in_sizes(list: list, size: int) -> list:
    return [list[i : i + size] for i in range(0, len(list), size)]


def intersect_lists(lists: list) -> list:
    return list(set(lists.pop()).intersection(*map(set, lists)))


# First part of challenge
with open("data.txt", encoding="utf-8") as file:
    bags = [split_in_half(line) for line in file.read().split("\n")]
    matches = [list(set(bag[0]).intersection(bag[1]))[0] for bag in bags]
    print(sum(symbols.index(e) + 1 for e in matches))

# Second part of challenge
with open("data.txt", encoding="utf-8") as file:
    groups = slpit_list_in_sizes([group for group in file.read().split("\n")], 3)
    print(sum(symbols.index(intersect_lists(group)[0]) + 1 for group in groups))
