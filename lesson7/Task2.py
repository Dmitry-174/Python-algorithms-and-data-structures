# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint, seed

length = 50  # длинна исходного массива
start = 0  # мин. значение в массиве
end = 49  # макс. значение в массиве

seed(42)
initial_list = [randint(start, end) for i in range(length)]


def mergesort_inplace(lst, start=0, end=None):
    """
    Отсортировать список методом слияния
    """
    def subpart(lst, start, end, pivot_index):
        lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
        pivot = lst[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if lst[y] <= pivot:
                lst[y], lst[x] = lst[x], lst[y]
                x += 1
            y += 1

        lst[start], lst[x - 1] = lst[x - 1], lst[start]
        return x - 1

    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return lst

    pivot_index = (start + end) // 2
    x = subpart(lst, start, end, pivot_index)
    mergesort_inplace(lst, start, x - 1)
    mergesort_inplace(lst, x + 1, end)

print(initial_list)
mergesort_inplace(initial_list)
print(initial_list)
