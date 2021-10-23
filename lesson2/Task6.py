# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
from random import randint

secret_num = randint(0, 100)
counter = 0
attempts = 10

while counter < attempts:
    user_num = int(input(f'Введите число (использовано {counter} попыток из {attempts}): '))
    counter += 1
    if user_num == secret_num:
        print(f"Вы угадали число за {counter} попыток")
        break
    elif user_num > secret_num:
        print(f'Выше число {user_num} больше загаданного')
    elif user_num < secret_num:
        print(f'Выше число {user_num} меньше загаданного')
else:
    print(f'Было загадано число {secret_num}')
