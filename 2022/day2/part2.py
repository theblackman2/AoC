tours = [line.split() for line in open("data.txt")]


def getValue(form: str, w: str):
    match w:
        case "X":
            if form == "A":
                return 3
            if form == "B":
                return 1
            if form == "C":
                return 2
        case "Y":
            if form == "A":
                return 4
            if form == "B":
                return 5
            if form == "C":
                return 6
        case "Z":
            if form == "A":
                return 8
            if form == "B":
                return 9
            if form == "C":
                return 7


sum = 0
for tour in tours:
    sum += getValue(tour[0], tour[1])

print(sum)
