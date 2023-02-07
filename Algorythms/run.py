from random import randint
from time import time

from bubble_sort import bubble_sort

def run_sorting(algorythm, array, reps):
    times = list()
    for i in range(reps):
        start = time()
        array = algorythm(array)
        times.append(time() - start)

    print(f"max: {max(times)}, min: {min(times)}.")


ARRAY_LENGTH = 1000

if __name__ == '__main__':
    reps = 10
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print('bubble_sort')
    run_sorting(algorythm=bubble_sort, array=array, reps=reps)
