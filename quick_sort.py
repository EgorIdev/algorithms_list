from random import randint
import time


start = time.time() ## точка отсчета времени
def quick(data):
    less = []
    pivotList = []
    more = []
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        for i in data:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick(less)
        more = quick(more)
        return less + pivotList + more

data = [randint(-500, 100000) for _ in range(100000)]
#quick(data)
print(quick(data)) ## вывод времени   0.277 seconds
end = time.time() - start ## собственно время работы программы
print(end)