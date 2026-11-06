from random import randint

numbers = [randint(0, 500) for _ in range(10)]
print("Before sorting:", numbers)


def bubble_sort(values):
    size = len(values)

    for step in range(size - 1):
        for index in range(size - step - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]

    return values


bubble_sort(numbers)

print("After sorting:", numbers)
