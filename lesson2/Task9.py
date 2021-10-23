# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def digit_sum(a):
    """Возвращает сумму цифр числа"""

    result = 0
    while a > 0:
        last_digit = a % 10
        result += last_digit
        a //= 10
    return result


n = int(input('Введите количество чисел в последовательности: '))
nums = [int(input(f'Введите {i + 1} число последовательности: ')) for i in range(n)]

max_num = 0
max_digit_sum = 0
for i in nums:
    digit_sum_i = digit_sum(i)
    if max_digit_sum < digit_sum_i:
        max_num = i
        max_digit_sum = digit_sum_i
print(max_num, max_digit_sum)
