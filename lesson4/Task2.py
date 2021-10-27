# 2 Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
import cProfile

n = 1000


def main(n):
    simple = [2]
    count = 1
    i = 3
    while count < n:
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break
        else:
            simple.append(i)
            count += 1
        i += 1
    print(simple[-1])


def eratosthenes(n):
    k = 4  # кратность длины изначального массива искомому n-му простому числу
    array = [i for i in range(2, k * n + 1)]
    while True:
        current_position = 0
        p = array[current_position]
        last_element = array[-1]
        while p < array[-1]:
            for i in array:
                if i == p:
                    continue
                if i % p == 0:
                    array.remove(i)
            current_position += 1
            p = array[current_position]
        if len(array) < n:
            array += [i for i in range(last_element + 1, last_element + k * n)]
        else:
            break
    print(array[n - 1])


cProfile.run('main(n)')
cProfile.run('eratosthenes(n)')

# в данном случае алгоритм нахождения n-ого простого числа без использования решета Эратосфена выполняется за 0.204с
# против 0.352с алгоритма с использованием решета. При этом 'remove' of 'list' objects занимает 0.184с (более 50 %)
# таким образом первый алгоритм работает эффективнее за счет того, что не требует хранения лишлих данных.

# недостатком алгоритма с использованием решета явлется невозможность определения оптимальной длины массива, для поиска
# n-ого простого числа (для поиска 10-го простого числа достаточно массива из 3 * n элементов,
# 100-ого - 5.5 * n элементов,  а 1000-го 8 * n элементов)
