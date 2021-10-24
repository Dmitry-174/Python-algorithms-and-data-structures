# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

lenght = 16  # длинна исходного массива
start = -20  # мин. значение в массиве
end = 20  # макс. значение в массиве


initial_list = [randint(start, end) for i in range(lenght)]

neg_elements = set()

for i in initial_list:
    if i < 0:
        neg_elements.add(i)
max_neg = max(neg_elements)
index = initial_list.index(max_neg)

print(initial_list)
print(f'В исходном списке наибольший отрицательный элемент = {max_neg}, его индекс = {index}')
