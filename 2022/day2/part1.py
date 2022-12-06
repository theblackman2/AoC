with open("data.txt", encoding="utf-8") as file:
    tours = [line.split() for line in file.read()]


def getFormValue(form: str):
    if form == "X":
        return 1
    if form == "Y":
        return 2
    if form == "Z":
        return 3


def getWonValue(elfForm: str, myForm: str):
    match elfForm:
        case "A":
            if myForm == "X":
                return 3
            if myForm == "Y":
                return 6
            return 0
        case "B":
            if myForm == "X":
                return 0
            if myForm == "Y":
                return 3
            return 6
        case "C":
            if myForm == "X":
                return 6
            if myForm == "Y":
                return 0
            return 3


sum = 0
for tour in tours:
    sum += getFormValue(tour[1]) + getWonValue(tour[0], tour[1])

print(sum)
