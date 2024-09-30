# Быстрая сортировка оптимизированная

list = [1, 5, 3, 7, 9, 4, 2, 6, 8, 0]

import random


def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        # Выбор случайного опорного элемента и его перемещение в начало
        pivot_index = random.randint(low, high)
        array[low], array[pivot_index] = array[pivot_index], array[low]

        # Разделение массива и получение позиции опорного элемента
        p = partition(array, low, high)

        # Рекурсивная сортировка подмассивов
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)
    return array


def partition(array, low, high):
    pivot = array[low]
    left = low + 1
    right = high

    while True:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[low], array[right] = array[right], array[low]
    return right

print(quick_sort(list))
