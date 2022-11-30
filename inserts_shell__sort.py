from random import randint


def shell(data):  # улучшенный вариант сортировки вставками
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


data = [randint(-500, 100000) for _ in range(100000)]
print(shell(data))
