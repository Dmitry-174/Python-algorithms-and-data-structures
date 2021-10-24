# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
from random import randint


def is_even(a):
    """Вазвращает True если число четное и наоборот"""

    if a % 2 == 0:
        return True
    else:
        return False


lenght = 16  # длинна исходного массива
start = 1  # мин. значение в массиве
end = 100  # макс. значение в массиве


initial_list = [randint(start, end) for i in range(lenght)]

result_list = []
for i, value in enumerate(initial_list):
    if is_even(value):
        result_list.append(i)

print(f'Исходный список {initial_list}')
print(f'Результирующий список {result_list}')
