money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
balance = money_capital + salary  # Начальный остаток средств
count = 0

while balance > spend:
    balance += salary - spend
    spend *= increase + 1
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
