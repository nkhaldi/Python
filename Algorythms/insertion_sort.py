def insertion_sort(array):
    for i in range(len(array)):
        j = i - 1
        key_item = array[i]

        while j >= 0 and array[j] > key_item:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key_item

    return array