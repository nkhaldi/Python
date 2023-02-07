def merge(array, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def merge_sort(array):
    if len(array) <= 1:
        return

    point = len(array) // 2
    left = array[:point]
    right = array[point:]

    merge_sort(left)
    merge_sort(right)
    merge(array, left, right)
