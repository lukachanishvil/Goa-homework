# განსაზღვრული მომხმარებლის სახელი და პაროლი
correct_username = "user123"
correct_password = "secure123"

# მომხმარებლის სახელი და პაროლის მოთხოვნა და შემოწმება
username = input("შეიყვანეთ მომხმარებლის სახელი: ")
password = input("შეიყვანეთ პაროლი: ")

while username != correct_username or password != correct_password:
    print("არასწორი მომხმარებლის სახელი ან პაროლი. გთხოვთ სცადოთ ისევ.")
    username = input("შეიყვანეთ მომხმარებლის სახელი: ")
    password = input("შეიყვანეთ პაროლი: ")

print("მიმართვა მიღებულია!")
