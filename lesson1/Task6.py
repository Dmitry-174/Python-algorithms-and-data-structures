# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

user_ord = int(input('Введите номер буквы в английском алфавите: '))
user_letter = chr(user_ord + 96)

print(f'{user_ord} буква английского алфавита - буква "{user_letter}"')
