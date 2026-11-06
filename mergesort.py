from random import randint

numbers = [randint(0, 500) for _ in range(10)]
print("Before sorting:", numbers)


def merge_sort(values, start, end):
    if start < end:
        middle = (start + end) // 2

        merge_sort(values, start, middle)
        merge_sort(values, middle + 1, end)

        merge_parts(values, start, middle, end)


def merge_parts(values, start, middle, end):
    left_part = values[start:middle + 1]
    right_part = values[middle + 1:end + 1]

    left_index = 0
    right_index = 0
    position = start

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            values[position] = left_part[left_index]
            left_index += 1
        else:
            values[position] = right_part[right_index]
            right_index += 1

        position += 1

    while left_index < len(left_part):
        values[position] = left_part[left_index]
        left_index += 1
        position += 1

    while right_index < len(right_part):
        values[position] = right_part[right_index]
        right_index += 1
        position += 1


merge_sort(numbers, 0, len(numbers) - 1)

print("After sorting:", numbers)
