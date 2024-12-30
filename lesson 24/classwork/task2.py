# მომხმარებლისგან ინფორმაციის შეყვანა
response = input("შეიყვანეთ ინფორმაცია ('yes' ან 'Yes'): ")

# პირობის შემოწმება და is_student ცვლადის შექმნა
if response == "yes" or response == "Yes":
    is_student = True
else:
    is_student = False

# შედეგის გამოტანა
print("is_student:", is_student)
