# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

lenght = 16  # длинна исходного массива
start = 1  # мин. значение в массиве
end = 20  # макс. значение в массиве


initial_list = [randint(start, end) for i in range(lenght)]

first_min = min(initial_list)
first_min_ind = initial_list.index(first_min)

second_min = max(initial_list)
for i, value in enumerate(initial_list):
    if i == first_min_ind:
        continue
    if value < second_min:
        second_min = value
print(initial_list)
print(f'Два наименьших элемента: {first_min}, {second_min}')
