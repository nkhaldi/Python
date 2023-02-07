from random import randint
from time import time

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

def run_sorting(algorythm, array, reps):
    times = list()
    for i in range(reps):
        start = time()
        array = algorythm(array)
        times.append(time() - start)

    print(f"max: {max(times)}, min: {min(times)}.")



if __name__ == '__main__':
    REPS, LENGTH = 10, 1000
    array = [randint(0, 1000) for i in range(LENGTH)]
    print('bubble_sort')
    run_sorting(algorythm=bubble_sort, array=array, reps=REPS)
    print('insertion_sort')
    run_sorting(algorythm=insertion_sort, array=array, reps=REPS)
