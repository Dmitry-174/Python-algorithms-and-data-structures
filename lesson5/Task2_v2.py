# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

a = list(input("Введите первое шестнадцатеричное число: ").upper())
b = list(input("Введите второе шестнадцатеричное число: ").upper())

hex_symbols = '0123456789ABCDEF'
d = {}
counter = 0
for key in hex_symbols:
    d[key] = counter
    counter += 1

d_inv = {}
for i in range(16):
    d_inv[i] = hex_symbols[i]


def to_dex(*args):
    """ Возвращает 10-чное число из 16-чного числа где каждый аргумент - цифра 16-чного числа """
    a10 = 0
    decimal = 1
    for i in args[::-1]:
        a10 += d[i] * decimal
        decimal *= 16
    return a10


def to_hex(a10):
    """ Возвращает 16-чное число как массив, элементы которого это цифры числа """
    a16 = deque()
    while a10:
        a16.appendleft(d_inv[a10 % 16])
        a10 //= 16
    return list(a16)


print(to_hex(to_dex(*a) + to_dex(*b)))
print(to_hex(to_dex(*a) * to_dex(*b)))
