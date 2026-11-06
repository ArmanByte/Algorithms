def build_prefix_table(pattern):
    prefix_table = [0] * len(pattern)
    prefix_length = 0

    for index in range(1, len(pattern)):
        while prefix_length > 0 and pattern[index] != pattern[prefix_length]:
            prefix_length = prefix_table[prefix_length - 1]

        if pattern[index] == pattern[prefix_length]:
            prefix_length += 1

        prefix_table[index] = prefix_length

    return prefix_table


def search_kmp(main_text, pattern):
    prefix_table = build_prefix_table(pattern)
    matches = []
    pattern_index = 0

    for text_index in range(len(main_text)):
        while pattern_index > 0 and main_text[text_index] != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index - 1]

        if main_text[text_index] == pattern[pattern_index]:
            pattern_index += 1

        if pattern_index == len(pattern):
            matches.append(text_index - len(pattern) + 1)
            pattern_index = prefix_table[pattern_index - 1]

    return matches


main_text = input("Enter text: ")
pattern = input("Enter pattern: ")

result = search_kmp(main_text, pattern)

print("Text:", main_text)
print("Pattern:", pattern)
print("Found at positions:", result)
