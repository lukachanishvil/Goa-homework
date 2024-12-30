# სიას შექმნა
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# მომხმარებლისგან ორი მთელი რიცხვის მიღება
num1 = int(input("შეიტანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიტანეთ მეორე რიცხვი (num2): "))

# ლოგიკა იმის მიხედვით, რომელი რიცხვი მეტია
if num1 > num2:
    new_list = my_list[num1:num2]
    print(new_list)
elif num2 > num1:
    new_list = my_list[num2:num1]
    print(new_list)
else:
    print([])  # ცარიელი სია
