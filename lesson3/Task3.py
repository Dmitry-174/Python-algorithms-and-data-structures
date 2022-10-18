# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

lenght = 16  # длинна исходного массива
start = 1  # мин. значение в массиве
end = 100  # макс. значение в массиве


initial_list = [randint(start, end) for i in range(lenght)]
result_list = initial_list.copy()

max_el, max_el_index = max(result_list), result_list.index(max(result_list))
min_el, min_el_index = min(result_list), result_list.index(min(result_list))

result_list[max_el_index], result_list[min_el_index] = min_el, max_el

print(initial_list)
print(result_list)
