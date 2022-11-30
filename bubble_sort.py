# Макс сложность O(N^2)
from random import randint


lst = [randint(-500, 10000) for _ in range(1000)]
n = len(lst)
for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)
