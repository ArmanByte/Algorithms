from random import randint

numbers = [randint(0, 500) for _ in range(10)]
print("Before sorting:", numbers)


def partition(values, start, end):
    pivot = values[end]
    smaller = start - 1

    for index in range(start, end):
        if values[index] <= pivot:
            smaller += 1
            values[smaller], values[index] = values[index], values[smaller]

    values[smaller + 1], values[end] = values[end], values[smaller + 1]

    return smaller + 1


def quick_sort(values, start, end):
    if start < end:
        pivot_position = partition(values, start, end)

        quick_sort(values, start, pivot_position - 1)
        quick_sort(values, pivot_position + 1, end)


quick_sort(numbers, 0, len(numbers) - 1)

print("After sorting:", numbers)
