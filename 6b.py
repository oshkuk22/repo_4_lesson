# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle

list_date = [1986, 1987,1988, 'day', 'mounth', 'year']

for i, name_list in enumerate(cycle(list_date)):
    print(i, name_list)
    if i == 200:
        break
