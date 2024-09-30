# Пузырьковая сортировка

list = [1, 5, 3, 7, 9, 4, 2, 6, 8, 0]

for i in range(len(list) - 1):
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)