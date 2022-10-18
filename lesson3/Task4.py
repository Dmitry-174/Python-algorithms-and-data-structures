# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

lenght = 16  # длинна исходного массива
start = 12  # мин. значение в массиве
end = 20  # макс. значение в массиве


initial_list = [randint(start, end) for i in range(lenght)]

count = 0
el = 0
for i in initial_list:
    current_count = initial_list.count(i)
    if current_count > count:
        count, el = current_count, i
print(initial_list)
print(f'В исходном списке число {el} встречается {count} раз')
