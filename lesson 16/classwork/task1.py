# მომხმარებლისგან რიცხვის მიღება
num = int(input("შეიტანეთ მთელი რიცხვი: "))

# რიცხვების ჯამის ინიციალიზაცია
sum_of_numbers = 0

# for ციკლი, რომელიც გადაამოწმებს ყველა რიცხვს 0-დან num-მდე
for i in range(num + 1):
    sum_of_numbers += i

# შედეგის დაბეჭდვა
print("დიაპაზონის 0-დან", num, "მდე ყველა რიცხვის ჯამი არის:", sum_of_numbers)
