# Сортировка выбором

list = [1, 5, 3, 7, 9, 4, 2, 6, 8, 0]

for i in range(len(list)):
    min_index = i
    for j in range(i + 1, len(list)):
        if list[j] < list[min_index]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[i]

print(list)