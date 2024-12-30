# სწორ პაროლს ვქმნით
correct_password = "mysecretpassword"

# პაროლის შესამოწმებლად ცვლადი
counter = 0

# while ციკლი, რომელიც განმეორებით ითხოვს პაროლს
while True:
    # მომხმარებლისგან პაროლის მოთხოვნა
    entered_password = input("შეიტანეთ პაროლი: ")
    
    # პაროლის შედარება
    counter += 1
    if entered_password == correct_password:
        print("Access granted")
        print("პაროლი შეიტანეთ", counter, "ჯერ.")
        break
    else:
        print("პაროლი არასწორია, სცადეთ კვლავ.")
