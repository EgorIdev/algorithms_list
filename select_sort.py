# Макс сложность O(N^2)
from random import randint


a = [randint(-500, 10000) for _ in range(1000)]
n = len(a)
for i in range(n - 1):
    m = a[i]  # минимальное значение
    p = i  # индекс минимального значения
    for j in range(i + 1, n):  # поиск миимального среди оставшихся элементов
        if m > a[j]:
            m = a[j]
            p = j

    if p != i:  # обмен значениями, если был найден минимальный не в i-й позиции
        t = a[i]
        a[i] = a[p]
        a[p] = t

print(a)
