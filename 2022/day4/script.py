with open("data.txt", encoding="utf-8") as file:
    data = file.read().strip()

sections = data.split("\n")

count1 = 0
count2 = 0

for section in sections:
    section1, section2 = section.split(",")
    section1_start, section1_end = map(int, section1.split("-"))
    section2_start, section2_end = map(int, section2.split("-"))

    if (section1_start <= section2_start and section2_end <= section1_end) or (
        section1_start >= section2_start and section2_end >= section1_end
    ):
        count1 += 1

    if set(range(section1_start, section1_end + 1)) & set(
        range(section2_start, section2_end + 1)
    ):
        count2 += 1

print(count1)
print(count2)
