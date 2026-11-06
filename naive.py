def search_naive(main_text, pattern):
    text_length = len(main_text)
    pattern_length = len(pattern)

    matches = []

    for position in range(text_length - pattern_length + 1):
        index = 0

        while index < pattern_length and main_text[position + index] == pattern[index]:
            index += 1

        if index == pattern_length:
            matches.append(position)

    return matches


main_text = input("Enter text: ")
pattern = input("Enter pattern: ")

result = search_naive(main_text, pattern)

print("Text:", main_text)
print("Pattern:", pattern)
print("Found at positions:", result)
