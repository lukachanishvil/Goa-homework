def manual_range(start, end, step):
    if step == 0:
        raise ValueError("Step არ შეიძლება იყოს 0")
    for number in range(start, end, step):
        if number % 2 == 0:
            print(number)

# ფუნქციის გამოძახება სხვადასხვა არგუმენტებით
manual_range(0, 10, 1)
manual_range(5, 20, 2)
manual_range(-10, 10, 3)
manual_range(2, 15, 4)
manual_range(10, 0, -2)
