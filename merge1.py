from random import randint
import time
from heapq import merge


start = time.time() ## точка отсчета времени
def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

m = [randint(-500, 100000) for _ in range(100000)]

end = time.time() - start ## собственно время работы программы
print(merge_sort(m)) ## вывод времени   0.0614 seconds
print(end)