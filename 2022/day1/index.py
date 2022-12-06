elfes = [line.split() for line in open("sample.txt")]

calories = []

index = 0
sum = 0
while True:
    if index == len(elfes):
        break
    if len(elfes[index]) == 0:
        calories.append(sum)
        sum = 0
        index += 1
        continue
    sum += int(elfes[index][0])
    index += 1

sortedCalories = sorted(calories)

print(sortedCalories[-1])
print(sortedCalories[-1] + sortedCalories[-2] + sortedCalories[-3])
