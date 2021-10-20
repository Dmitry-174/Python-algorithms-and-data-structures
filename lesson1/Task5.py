# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между
# ними находится букв.

letter_1 = input('Введите букву английского алфавита: ').lower()
letter_1_ord = ord(letter_1) - 96
letter_2 = input('Введите букву английского алфавита: ').lower()
letter_2_ord = ord(letter_2) - 96
letters_between = abs(letter_1_ord - letter_2_ord) - 1

print(f"Буква {letter_1} - {letter_1_ord} буква алфавита, буква {letter_2} - {letter_2_ord} буква алфавита")
print(f"Между буквой {letter_1} и буквой {letter_2} - {letters_between} букв ")
