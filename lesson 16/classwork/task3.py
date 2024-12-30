import random

# შემთხვევითი რიცხვის შექმნა 1-დან 10-მდე
my_num = random.randint(1, 10)

# ცდების დათვლა
attempts = 0

# while ციკლი, რომელიც ითხოვს მომხმარებლის მიერ შეყვანილ რიცხვს
while True:
    # მომხმარებლისგან რიცხვის მოთხოვნა
    guess = int(input("გთხოვთ, შეიტანეთ რიცხვი 1-დან 10-მდე: "))
    
    # ცდების რაოდენობის გაზრდა
    attempts += 1
    
    # რიცხვის შედარება
    if guess == my_num:
        print(f"You guessed it! You guessed the number in {attempts} attempts.")
        break
    else:
        print("არასწორი რიცხვია, სცადეთ კიდევ.")
