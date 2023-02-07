from random import randint
from time import time

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def run_sorting(algorythm, length, reps):
    times = list()

    for _ in range(reps):
        array = [randint(0, 1000) for _ in range(length)]
        start = time()
        array = algorythm(array)
        times.append(time() - start)

    print(f"max: {max(times)}, min: {min(times)}.\n")


if __name__ == '__main__':
    LENGTH, REPS = 10, 10
    print('bubble_sort')
    run_sorting(algorythm=bubble_sort, length=LENGTH, reps=REPS)
    print('insertion_sort')
    run_sorting(algorythm=insertion_sort, length=LENGTH, reps=REPS)
    print('merge_sort')
    run_sorting(algorythm=merge_sort, length=LENGTH, reps=REPS)
    print('quick_sort')
    run_sorting(algorythm=quick_sort, length=LENGTH, reps=REPS)
