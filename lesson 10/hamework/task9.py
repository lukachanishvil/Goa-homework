# მომხმარებლისგან ორი რიცხვის მიღება
num1 = float(input("გთხოვთ, შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("გთხოვთ, შეიყვანეთ მეორე რიცხვი: "))

# ჯამი
sum_result = num1 + num2

# სხვაობა
difference = num1 - num2

# ნამრავლი
product = num1 * num2

# განაყოფი (დაშლა)
if num2 != 0:
    division = num1 / num2
else:
    division = "არ შეიძლება, რიცხვი 0-ით დაყოფა"

# პირველი რიცხვის ხარისხად მეორე რიცხვი
if num2 != 0:
    first_to_second = num1 / num2
else:
    first_to_second = "არ შეიძლება, რიცხვი 0-ით დაყოფა"

# მეორე რიცხვის ხარისხად პირველი რიცხვი
if num1 != 0:
    second_to_first = num2 / num1
else:
    second_to_first = "არ შეიძლება, რიცხვი 0-ით დაყოფა"

# შედეგების დაბეჭდვა
print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference}")
print(f"ნამრავლი: {product}")
print(f"განაყოფი: {division}")
print(f"პირველი რიცხვი ხარისხად მეორეზე: {first_to_second}")
print(f"მეორე რიცხვი ხარისხად პირველზე: {second_to_first}")
