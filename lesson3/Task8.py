# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
from copy import deepcopy
from random import randint

rows = 4  # количество строк матрицы
columns = 4  # количество столбцов матрицы
start = 1  # мин. значение в массиве
end = 20  # макс. значение в массиве


initial_list = [[randint(start, end) for i in range(columns)] for j in range(rows)]
result_list = deepcopy(initial_list)

for i in result_list:
    i.append(sum(i))

for i in result_list:
    for j in i:
        print(j, end='\t')
    print()
