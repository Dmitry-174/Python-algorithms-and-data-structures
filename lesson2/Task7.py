# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def progr_sum(n):
    """Рекурсивная функция, возвращает сумму n элементов последовательности"""

    if n == 1:
        return n
    else:
        return n + progr_sum(n - 1)


n = int(input("Введите количество элементов полседовательности: "))

sum_rec = progr_sum(n)
sum_eq = n * (n + 1) / 2

if sum_rec == sum_eq:
    print('1+2+...+n = n(n+1)/2 - Верно')

else:
    print('1+2+...+n = n(n+1)/2 - Не верно')

# вариант через цикл для чисел больше 996
sum_loop = 0
for i in range(1, n + 1):
    sum_loop += i
if sum_loop == sum_eq:
    print('1+2+...+n = n(n+1)/2 - Верно')

else:
    print('1+2+...+n = n(n+1)/2 - Не верно')
