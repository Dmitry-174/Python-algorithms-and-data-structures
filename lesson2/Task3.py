# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


user_num = int(input("Введите натуральное число: "))
user_num = int(user_num)
reverse_num = []

while user_num > 0:
    last_digit = user_num % 10
    reverse_num.append(last_digit)
    user_num //= 10

int_reverse_num = 0
for i, value in enumerate(reverse_num):
    int_reverse_num += value * 10 ** (len(reverse_num) - 1 - i)
print(int_reverse_num)