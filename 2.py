"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор."""

list_numbers = [8, 1000, 9, 7, 9, 10, 16, 65, 56, 7, 100]

list_sort_numbers = [list_numbers[el_list + 1]
                     for el_list in range(len(list_numbers) - 1)
                     if list_numbers[el_list + 1] > list_numbers[el_list]]

print(list_sort_numbers)
