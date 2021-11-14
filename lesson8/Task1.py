# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке
import hashlib
from random import randint, seed

length = 10  # длинна строки
start = 'a'  # начальный символ
end = 'z'  # конечный символ

seed(42)
initial_string = ''.join([chr(randint(ord(start), ord(end))) for i in range(length)])
print(initial_string)

substrings = set()
counter = 0
for i in range(len(initial_string)):
    for j in range(len(initial_string), i, -1):
        hash_string = hashlib.sha1(initial_string[i:j].encode('utf-8')).hexdigest()
        substrings.add(hash_string)
        counter += 1

print(f'Всего {counter} подстрок')
print(f'Уникальных {len(substrings)} подстрок')
