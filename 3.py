"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор"""

list_numbers = [numbers for numbers in range(20, 241, 1) if numbers % 20 == 0 or numbers % 21 == 0]

print(list_numbers)
