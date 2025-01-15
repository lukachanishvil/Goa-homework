def manual_find(main_string, str_to_find):
    # დავალების შესრულება ინდექსის მოძიებით
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i + len(str_to_find)] == str_to_find:
            return i
    return -1  # თუ ვერ მოიძებნა, ვაბრუნებთ -1-ს

# ფუნქციის ტესტი
main_string = input("შეიყვანეთ მთავარი ტექსტი: ")
str_to_find = input("რა ტექსტი უნდა მოიძებნოს? ")

# შედეგის დაბეჭდვა
result = manual_find(main_string, str_to_find)
print(result)
