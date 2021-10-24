# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from copy import deepcopy
from random import randint

rows = 4  # количество строк матрицы
columns = 4  # количество столбцов матрицы
start = 1  # мин. значение в массиве
end = 20  # макс. значение в массиве


initial_list = [[randint(start, end) for i in range(columns)] for j in range(rows)]
result_list = deepcopy(initial_list)

min_elemets = set()
for j in range(len(result_list[0])):
    column = []
    for i in result_list:
        column.append(i[j])
    min_elemets.add(min(column))

print(initial_list)
print(max(min_elemets))
