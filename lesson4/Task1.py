# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

from random import randint, seed
import cProfile

lenght = 10000000  # длинна исходного массива
start = 1  # мин. значение в массиве
end = 10000000  # макс. значение в массиве

initial_list = [randint(start, end) for i in range(lenght)]
seed(42)

def main(initial_list):
    first_min = min(initial_list)
    first_min_ind = initial_list.index(first_min)

    second_min = max(initial_list)
    for i, value in enumerate(initial_list):
        if i == first_min_ind:
            continue
        if value < second_min:
            second_min = value

    print(f'Два наименьших элемента: {first_min}, {second_min}')

def main2(initial_list):
    sorted_list = sorted(initial_list)
    print(f'Два наименьших элемента: {sorted_list[0]}, {sorted_list[1]}')


cProfile.run('main(initial_list)')
cProfile.run('main2(initial_list)')

# При lenght = 10000000:
# выполнение первого алгоритма заняло 1.971с:
# main - 1.971с; max - 0.252; min - 0.254; index - 0.204
# выполнение второго алгоритма заняло 8.275с:
# main2 - 7.866; sorted - 7.865 (почти 100% от main2)

# При lenght = 20000000:
# выполнение первого алгоритма заняло 3.917с:
# main - 3.916с; max - 0.496; min - 0.495; index - 0.315
# выполнение второго алгоритма заняло 8.275с:
# main2 - 17.823; sorted - 17.823 (100% от main2)

# при увеличении длины массива в 2 раза, время выполнения первого алгоритма увеличилось в 1,99 раз
# а второго в 2,29 раз
# сложность первого алгоритма = O(n), а второго = O(n**2) из-за наличия алгоритма сортировки (на конкретном примере
# приблизительно O(n**1.2)
