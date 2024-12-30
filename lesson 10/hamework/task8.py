# მომხმარებლისგან სამი რიცხვის მიღება
num1 = float(input("გთხოვთ, შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("გთხოვთ, შეიყვანეთ მეორე რიცხვი: "))
num3 = float(input("გთხოვთ, შეიყვანეთ მესამე რიცხვი: "))

# ჯამი
sum_result = num1 + num2 + num3

# სხვაობა (განსხვავება პირველი რიცხვისა და დანარჩენების შორის)
difference = num1 - num2 - num3

# ნამრავლი
product = num1 * num2 * num3

# განაყოფი (პირველი რიცხვი დანარჩენებისგან)
if num2 != 0 and num3 != 0:
    division = num1 / num2 / num3
else:
    division = "არ შეიძლება, რიცხვი 0-ით დაყოფა"

# შედეგების დაბეჭდვა
print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference}")
print(f"ნამრავლი: {product}")
print(f"განაყოფი: {division}")
