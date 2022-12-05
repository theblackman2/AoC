import string

with open("test.txt", encoding="utf_8") as file:
    data = file.read()

symbols = [letter for letter in string.ascii_letters]

columns = [d for d in data.split("\n\n")[0].splitlines()]
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
print(ranges)
