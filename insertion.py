from random import randint

numbers = [randint(0, 500) for _ in range(10)]
print("Before sorting:", numbers)


def insertion_sort(values):
    for position in range(1, len(values)):
        current_value = values[position]
        index = position - 1

        while index >= 0 and values[index] > current_value:
            values[index + 1] = values[index]
            index -= 1

        values[index + 1] = current_value

    return values


insertion_sort(numbers)

print("After sorting:", numbers)
