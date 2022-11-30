# Макс сложность O(N^2)
from random import randint


def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq


seq = [randint(-500, 10000) for _ in range(1000)]
print(bubble_sort(seq))
