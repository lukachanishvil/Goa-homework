def generate_big_sentence(name, surname, age):
    print("My name is {}, my surname is {}, and I am {} years old.".format(name, surname, age))

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

generate_big_sentence(name, surname, age)
