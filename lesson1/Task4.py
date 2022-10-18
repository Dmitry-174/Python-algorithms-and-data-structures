# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
from random import choice, randint, uniform

action = int(input('1 - случайное целое число, 2 - случайное вещественное число, 3 - случайный символ: '))
a = input('Введите первую границу: ')
b = input('Введите вторую границу: ')

if action == 1:
    a, b = int(a), int(b)
    left = min(a, b)
    right = max(a, b)
    result = randint(left, right)

elif action == 2:
    a, b = float(a), float(b)
    left = min(a, b)
    right = max(a, b)
    result = uniform(left, right)

elif action == 3:
    left = min(ord(a), ord(b))
    right = max(ord(a), ord(b))
    result = choice([chr(i) for i in range(left, right + 1)])

else:
    print('Неверный выбор действия')

print(result)
