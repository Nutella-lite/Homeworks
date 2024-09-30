Вот некоторые из известных алгоритмов сортировки:

1. **Пузырьковая сортировка (Bubble Sort)**
2. **Сортировка выбором (Selection Sort)**
3. **Сортировка вставками (Insertion Sort)**
4. **Сортировка слиянием (Merge Sort)**
5. **Быстрая сортировка (Quick Sort)**
6. **Сортировка кучей (Heap Sort)**
7. **Сортировка подсчётом (Counting Sort)**
8. **Поразрядная сортировка (Radix Sort)**
9. **Сортировка Шелла (Shell Sort)**
10. **Сортировка корзинами (Bucket Sort)**
11. **Timsort** (используется в Python по умолчанию)

Ниже приведены примеры реализации некоторых из этих алгоритмов на Python.

---

### 1. Пузырьковая сортировка (Bubble Sort)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

**Пример использования:**

```python
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
```

---

### 2. Сортировка выбором (Selection Sort)

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Обмен элемента минимального с первым элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

### 3. Сортировка вставками (Insertion Sort)

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы, которые больше ключа, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

### 4. Сортировка слиянием (Merge Sort)

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Рекурсивное разделение
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Слияние временных массивов
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

---

### 5. Быстрая сортировка (Quick Sort)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
```

**Пример использования:**

```python
arr = [10, 7, 8, 9, 1, 5]
arr = quick_sort(arr)
print(arr)
```

---

### 6. Сортировка кучей (Heap Sort)

```python
def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # левый = 2*i + 1
    r = 2 * i + 2  # правый = 2*i + 2

    # Проверяем, существует ли левый дочерний элемент больше корня
    if l < n and arr[largest] < arr[l]:
        largest = l

    # Проверяем, существует ли правый дочерний элемент больше корня
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # свап

        # Рекурсивно heapify поддерево
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)
```

---

### 7. Сортировка подсчётом (Counting Sort)

```python
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Инициализация счётного массива
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # Подсчёт каждого элемента
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_val] += 1

    # Изменение count_arr чтобы содержать позиции элементов в output_arr
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Построение output_arr
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    # Копирование output_arr в arr
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
```

---

### 8. Поразрядная сортировка (Radix Sort)

```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # выходной массив
    count = [0] * 10  # для цифр 0-9

    # Подсчитываем количество вхождений в count[]
    for i in range(0, n):
        index = arr[i] // exp
        count[(index) % 10] += 1

    # Изменяем count[i] так, чтобы он содержал актуальную позицию цифры
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Строим выходной массив
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # Копируем выходной массив в arr[]
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Находим максимальное число чтобы знать количество цифр
    max1 = max(arr)

    # Применяем counting sort для каждой цифры
    exp = 1
    while max1 / exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
```

---

### 9. Сортировка Шелла (Shell Sort)

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Начинаем с большого промежутка, затем уменьшаем его
    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            # Сдвигаем элементы arr[0..i-gap], которые больше temp
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2
```

---

### 10. Сортировка корзинами (Bucket Sort)

```python
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Определяем количество корзин
    bucket_count = len(arr)
    max_value = max(arr)
    min_value = min(arr)

    # Создаем корзины
    buckets = [[] for _ in range(bucket_count)]

    # Распределяем элементы по корзинам
    for i in range(len(arr)):
        index = int((arr[i] - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(arr[i])

    # Сортируем каждую корзину и объединяем
    arr.clear()
    for bucket in buckets:
        insertion_sort(bucket)  # Можно использовать любую сортировку внутри корзины
        arr.extend(bucket)
```

---

### 11. Использование встроенной сортировки Python (Timsort)

```python
arr.sort()
```

**Пример использования:**

```python
arr = [5, 2, 9, 1, 5, 6]
arr.sort()
print(arr)
```

**Примечание:** Встроенная функция `sort()` в Python использует алгоритм Timsort, который является гибридом сортировки слиянием и вставками и хорошо оптимизирован для реальных данных.

---

