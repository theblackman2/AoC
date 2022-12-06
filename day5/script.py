import string


def move_stuffs(gesture: string, data: list) -> list:
    move = [int(g) for g in gesture if g.isnumeric()]
    f: int = move[1] - 1
    t: int = move[2] - 1

    from_list: list = data[f]
    nbr_to_move: int = move[0]
    to_list: list = data[t]
    # print(from_list, nbr_to_move, to_list)

    elements_to_move: list = from_list[0:nbr_to_move]
    # print(elements_to_move.reverse())
    elements_to_move.reverse()
    # print(elements_to_move)

    from_list = from_list[nbr_to_move:]
    to_list = [*elements_to_move, *to_list]
    data[f] = from_list
    data[t] = to_list
    return data


with open("data.txt", encoding="utf_8") as file:
    data = file.read()

symbols = [letter for letter in string.ascii_letters]

columns = [d for d in data.split("\n\n")[0].splitlines()]

moves = [m for m in data.split("\n\n")[1].splitlines()]

columns.pop()
max = max(len(a) for a in columns)
ranges = []
for i in range(max // 3):
    ranges.append([])

for column in columns:
    last_index = len(column)
    for i in range(1, last_index, 4):
        if column[i] in symbols:
            index = (i - 1) // 3
            ranges[index].append(column[i])

# print(ranges)

for move in moves:
    # print(move)
    ranges = move_stuffs(move, ranges)

for r in ranges:
    if len(r) > 0:
        print(r[0])
