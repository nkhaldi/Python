from random import randint


def quick_sort(array):
    if len(array) <= 1:
        return array

    left, mid, right = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for elem in array:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            mid.append(pivot)

    return quick_sort(left) + mid + quick_sort(right)
