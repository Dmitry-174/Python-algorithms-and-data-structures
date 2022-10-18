# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

initial_string = 'самая любая строка'

table = {i: initial_string.count(i) for i in initial_string}
print(table)

# дерево в виде картинки прилагаю
