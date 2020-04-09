"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться
следующим образом: for el in fibo_gen(). Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

from functools import  reduce

def factorial_numbers(number_):
    for j in range(1, number_+1):
        yield j

count_fact = 15

for number in range(count_fact+1):
    if number == 0:
        print(f'{number}! = 1')
    else:
        print(f'{number}! = {reduce(lambda x, y: x*y, [x for x in factorial_numbers(number)])}')

# pull requests

