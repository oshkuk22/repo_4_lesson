# а) бесконечный итератор, генерирующий целые числа, начиная с указанного.

from itertools import count

for i in count(start=6000, step=1):
    print(i)
    if i == 100000:
        break



