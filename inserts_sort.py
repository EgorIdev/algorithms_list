# Макс сложность O(N^2)
from random import randint


a = [randint(-500, 100000) for _ in range(10000)]
n = len(a)
for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break
print(a)
