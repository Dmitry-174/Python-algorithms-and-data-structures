# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите количество вводимых чисел: '))
digit = input('Введите искомую цифру: ')
counter = 0

subsequence = [input(f'Введите {i} число последовательности: ') for i in range(1, n + 1)]
for i in subsequence:
    counter += i.count(digit)

print(counter)
