while True:
    days = 1
    km_in = float(input("Введите количество километров, которое Вы пробежали сегодня: "))
    km_end = float(input("Введите количество километров, которое Вы  желаете достичь: "))
    while km_in < km_end:
        km_in += km_in * 0.1
        days = days + 1
        print(f"Вы достигните желаемого результата через {days} дней")
    break
