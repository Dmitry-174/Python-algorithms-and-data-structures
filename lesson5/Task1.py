# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

n = int(input('Введите количество предприятий: '))
enterprises = {input('Введите наименование предприятия: '):
                   {'quarters': [int(j) for j in input('Введите через пробел прибыль по кварталам: ').split()]}
               for i in range(n)}

total_profit = 0

for enterprise, profit in enterprises.items():
    if len(profit['quarters']) == 4:
        profit['year'] = sum(profit['quarters'])
        total_profit += profit['year']
    else:
        raise Exception(f'Неверно заполнена прибыль по кварталам для {enterprise}')

avg = total_profit / len(enterprises)

below_avg = []
above_avg = []

for enterprise, profit in enterprises.items():
    if profit['year'] >= avg:
        above_avg.append(enterprise)
    else:
        below_avg.append(enterprise)

print('Прибыль выше средней (или равна средней) у предприятий:', *above_avg)
print('Прибыль ниже средней у предприятий:', *below_avg)
