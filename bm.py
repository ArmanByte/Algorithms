def create_shift_table(pattern):
    shift_table = {}

    for index, char in enumerate(pattern):
        shift_table[char] = index

    return shift_table


def search_pattern(main_text, pattern):
    text_length = len(main_text)
    pattern_length = len(pattern)

    shift_table = create_shift_table(pattern)
    found_positions = []

    start = 0

    while start <= text_length - pattern_length:
        current = pattern_length - 1

        while current >= 0 and pattern[current] == main_text[start + current]:
            current -= 1

        if current < 0:
            found_positions.append(start)
            start += 1
        else:
            mismatch_char = main_text[start + current]
            last_index = shift_table.get(mismatch_char, -1)

            start += max(1, current - last_index)

    return found_positions


main_text = input("Enter text: ")
pattern = input("Enter pattern: ")

matches = search_pattern(main_text, pattern)

print("Text:", main_text)
print("Pattern:", pattern)
print("Found at positions:", matches)
