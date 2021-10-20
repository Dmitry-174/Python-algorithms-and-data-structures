# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_num = int(input('Введите трехзначное число'))
a = user_num // 100
b = user_num % 100 // 10
c = user_num % 10
sum = a + b + c
prod = a * b * c
print(f'Сумма цифр числа {user_num} = {sum}')
print(f'Произведение цифр числа {user_num} = {prod}')
