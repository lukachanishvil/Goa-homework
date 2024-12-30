# მომხმარებლისგან რიცხვის მიღება
number = int(input("შეიყვანეთ რიცხვი: "))

# ფაქტორალის თავდაპირველი მნიშვნელობა
factorial = 1

# while ციკლი ფაქტორალის გამოთვლისთვის
while number > 1:
    factorial *= number
    number -= 1  # რიცხვის შემცირება თითოეულ გამეორებაზე

print(f"წარმოების ფაქტორალი: {factorial}")




# მოთხოვნა მომხმარებლისგან
number = int(input("შეიყვანეთ რიცხვი, რომლის ფაქტორიალს გსურთ გაანგარიშება: "))

# ინიციალიზაცია
factorial = 1
counter = number

# while ციკლი ფაქტორიალის გამოთვლისთვის
while counter > 1:
    factorial *= counter
    counter -= 1

# შედეგის გამოყვანა
print(f"{number}-ის ფაქტორიული არის: {factorial}")
