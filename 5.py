"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

# first way
list_numbers = [numbers for numbers in range(100, 1001, 2)]

# second way
#list_numbers = [numbers for numbers in range(100, 1001) if numbers % 2 == 0]

myltiply_list = reduce(lambda el_1, el_2: el_1*el_2, list_numbers)
print(myltiply_list)

