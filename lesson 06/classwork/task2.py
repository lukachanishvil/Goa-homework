1. #"Hello World" ვერ დაიბეჭდება სწორი სინტაქსით.
# print "Hello World"  # შეცდომა: Python 3-ში უნდა იქნას გამოყენებული ტრუიული სიმბოლოები (" ")

# 2. ცვლადი არ არის განსაზღვრული, მაგრამ გამოყენებულია
# print(variable)  # შეცდომა: variable არ არის განსაზღვრული

# 3. არასწორად დახურული სტრიქონი
# print("Hello World"  # შეცდომა: სტრიქონი არ არის დახურული

# 4. ამინდებული სტრიქონი
print("This is an indented line")  # სწორი სინტაქსი

# 5. განუცხადებული ცვლადი
# print(undeclared_variable)  # შეცდომა: undeclared_variable არ არსებობს

# 6. "class" არის რეზერვირებული სიტყვა, არ შეიძლება მისი გამოყენება ცვლადად
# class = 5  # შეცდომა: "class" არის რეზერვირებული სიტყვა

# 7. დახურული სტრიქონის პრობლემა
# print("Hello World')  # შეცდომა: სტრიქონი არ არის სწორად დახურული

# 8. ცვლადების სახელები არ შეიძლება დაიწყებოდეს რიცხვით
# 1var = 10  # შეცდომა: ცვლადი ვერ დაიწყება რიცხვით

# 9. ცვლადების სხვადასხვა ტიპის მონაცემების დამატება
x = 10
y = "5"
# print(x + y)  # შეცდომა: არ შეიძლება integer და string-ის ჯამი; საჭიროა int(y) გამოყენება.

# 10. ფუნქციაში ინდენტაციის შეცდომა
def my_function():
    print("Missing indentation in function")  # უნდა იყოს სწორად აწყობილი ინდენტაცია

# 11. ცვლადის სახელში სიმბოლოები არ შეიძლება იყოს რიცხვი
# 1var = 10  # შეცდომა: ცვლადი ვერ დაიწყება რიცხვით

# 12. არმოყვანილი სტრიქონი
# print("Unclosed string  # შეცდომა: სტრიქონი არ არის დახურული

# 13. წყვილი ციტატების გამოყენება
print("Escaped quote: \" ")  # Escaped quote: "

# 14. "True" არის რეზერვირებული სიტყვა
# True = 5  # შეცდომა: "True" არის რეზერვირებული სიტყვა

# 15. კომენტარის სიმბოლო არ არის
# This is a comment  # შეცდომა: არ არის კომენტარი, რადგან არ არის "#" სიმბოლო

# 16. if-განაცხადი არ არის სრულად
# if True
# print("No colon in if statement")  # შეცდომა: აკლია ":" if-განაცხადში

# 17. ფუნქცია არ აქვს სწორი indentაცია
def add(a, b):
    return a + b  # ფუნქცია უნდა იყოს სწორად გაწყობილი

# 18. ცვლადის დეფინიცია არ არის
# variable  # ცვლადი არ არის განსაზღვრული

# 19. ცარიელი შინაარსი
# print("Empty statement after variable declaration") 