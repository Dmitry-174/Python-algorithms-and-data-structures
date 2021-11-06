from random import randint, seed
import memory_profiler

lenght = 500000  # длинна исходного массива
start = 1  # мин. значение в массиве
end = 500000  # макс. значение в массиве

initial_list = [randint(start, end) for i in range(lenght)]
seed(42)


@profile
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


@profile
def main2(initial_list):
    sorted_list = sorted(initial_list)
    print(f'Два наименьших элемента: {sorted_list[0]}, {sorted_list[1]}')


if __name__ == '__main__':
    main(initial_list)
    main2(initial_list)

# OS: Windows 7 64-bit
# Python 3.8
#
# Результаты:
# Filename: lesson6\Task1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12   38.375 MiB   38.375 MiB           1   @profile
#     13                                         def main(initial_list):
#     14   38.379 MiB    0.004 MiB           1       first_min = min(initial_list)
#     15   38.383 MiB    0.004 MiB           1       first_min_ind = initial_list.index(first_min)
#     16
#     17   38.383 MiB    0.000 MiB           1       second_min = max(initial_list)
#     18   38.457 MiB    0.020 MiB      500001       for i, value in enumerate(initial_list):
#     19   38.457 MiB    0.016 MiB      500000           if i == first_min_ind:
#     20   38.457 MiB    0.000 MiB           1               continue
#     21   38.457 MiB    0.039 MiB      499999           if value < second_min:
#     22   38.457 MiB    0.000 MiB          13               second_min = value
#     23
#     24   38.465 MiB    0.008 MiB           1       print(f'Два наименьших элемента: {first_min}, {second_min}')
#
#
# Filename: lesson6\Task1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     27   38.469 MiB   38.469 MiB           1   @profile
#     28                                         def main2(initial_list):
#     29   42.535 MiB    4.066 MiB           1       sorted_list = sorted(initial_list)
#     30   42.535 MiB    0.000 MiB           1       print(f'Два наименьших элемента: {sorted_list[0]}, {sorted_list[1]}')
