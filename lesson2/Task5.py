# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

start = 32
end = 127
e = '\t'
printed = 0
for i in range(start, end + 1):
    if printed == 9:
        e = '\n'
    elif printed == 10:
        e = '\t'
        printed = 0
    print(f'{i}-{chr(i)}', end=e)
    printed += 1