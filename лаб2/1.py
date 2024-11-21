money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

remainder = money_capital + salary - spend   # Остаток в первый месяц
k = 1   # Количество месяцев
a = spend + spend * increase   # Повышеная сумма трат

while remainder > 0:
    k += 1
    remainder = remainder + salary - a
    a = a + a * increase

print(f"Количество месяцев, которое можно протянуть без долгов: {k-1}")

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


