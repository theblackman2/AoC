elfes = [l.split() for l in open("data.txt")]

calories = []

index = 0
sum = 0
while True:
    if index == len(elfes) - 1:
        break
    if len(elfes[index]) == 0:
        calories.append(sum)
        sum = 0
        index += 1
        continue
    sum += int(elfes[index][0])
    index += 1

print(sorted(calories)[-1])
