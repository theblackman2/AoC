def contains_unique_values(data: list) -> bool:
    return len(data) == len(set(data))


def get_last_buffer_part_index(buffer: list, iterations: int) -> int | None:
    for i in range(0, len(buffer)):
        last_index = i + iterations
        buffer_part = buffer[i:last_index]
        if contains_unique_values(buffer_part):
            return last_index
    return None


with open("data.txt", encoding="utf-8") as file:
    buffer = file.read()

# First part
print(get_last_buffer_part_index(buffer, 4))

# Second part
print(get_last_buffer_part_index(buffer, 14))
