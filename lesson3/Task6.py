# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

lenght = 16  # длинна исходного массива
start = 1  # мин. значение в массиве
end = 100  # макс. значение в массиве


initial_list = [randint(start, end) for i in range(lenght)]

max_el_index = initial_list.index(max(initial_list))
min_el_index = initial_list.index(min(initial_list))

total = sum(initial_list[max_el_index + 1:min_el_index]) if max_el_index < min_el_index else\
    sum(initial_list[min_el_index + 1:max_el_index])

print(initial_list)
print(f'Сумма чисел между мин. и макс. элементами = {total}')
