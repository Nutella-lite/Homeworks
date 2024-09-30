# Быстрая сортировка

list = [1, 5, 3, 7, 9, 4, 2, 6, 8, 0]

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_equal = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less_equal) + [pivot] + quick_sort(greater)

print(quick_sort(list))