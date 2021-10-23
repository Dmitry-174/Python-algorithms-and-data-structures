# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def is_even(a):
    """Вазвращает True если число четное и наоборот"""

    if a % 2 == 0:
        return True
    else:
        return False


user_num = [int(i) for i in input('Введите натуральное число: ')]
even = 0
not_even = 0

for i in user_num:
    if is_even(i):
        even += 1
    else:
        not_even += 1
print(f"{even} четных цифр и {not_even} нечетных")
