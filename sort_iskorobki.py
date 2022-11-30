from random import randint
import time


start = time.time() ## точка отсчета времени

data = [randint(-500, 100000) for _ in range(100000)]
data.sort()
end = time.time() - start ## собственно время работы программы
print(end) ## вывод времени   0.0773 seconds