# განსაზღვრული პაროლი
correct_password = "secure123"

# მომხმარებლისგან პაროლის მოთხოვნა და შემოწმება
user_password = input("Enter the password: ")

while user_password != correct_password:
    print("Incorrect password. Please try again.")
    user_password = input("Enter the password: ")

print("Access granted!")
