def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        item = array[i]

        while j >= 0 and array[j] > item:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = item

    return array
