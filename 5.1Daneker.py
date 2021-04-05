income = int(input("Введите значение выручки в рублях: "))
expenditure = int(input("Введите значение издержек в рублях: "))

amount = income - expenditure
if amount > 0:
    revenue = amount / income * 100
    stuff = int(input("Введите количество нанятых работников: "))
    amountperperson = amount / stuff
    print(f"Ваша прибыль: {amount}, Ваша рентабельность выручки: {revenue} %, Ваша прибыль на одного нанятого сотрудника {amountperperson}")
elif amount < 0:
    print(f"Ваши убытки: {amount}")
else:
    print("Ваша компания вышла в ноль")