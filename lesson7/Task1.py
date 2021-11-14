# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint, seed

length = 100  # длинна исходного массива
start = -100  # мин. значение в массиве
end = 99  # макс. значение в массиве

seed(42)
initial_list = [randint(start, end) for i in range(length)]


def bubble_sort(initial_list):
    n = 1
    while n < len(initial_list):
        transpositions = 0
        for i in range(len(initial_list) - n):
            if initial_list[i] < initial_list[i + 1]:
                initial_list[i], initial_list[i + 1] = initial_list[i + 1], initial_list[i]
                transpositions += 1
        if transpositions == 0:
            break
        n += 1


print(initial_list)
bubble_sort(initial_list)
print(initial_list)
