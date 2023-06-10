def selection_sort(array):
    n = len(array)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if array[j] < array[k]:
                k = j

        array[i], array[k] = array[k], array[i]

    return array
