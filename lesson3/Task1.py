# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
start = 2
end = 99
dividends = [i for i in range(2, 100)]
divisors = [i for i in range(2, 10)]

counter = 0

for i in divisors:
    for j in dividends:
        if j % i == 0:
            counter += 1
    print(f'В диапазоне от {start} до {end} - {counter} чисел кратны {i}')
    counter = 0
