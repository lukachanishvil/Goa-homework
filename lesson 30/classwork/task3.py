# მომხმარებლისგან მონაცემების მიღება
main_str = input("შეიყვანეთ მთავარი სთრინგი: ")
str_to_count = input("შეიყვანეთ დასათვლელი სთრინგი: ")

# str_to_count-ის რაოდენობის დათვლა main_str-ში
count = main_str.count(str_to_count)

# შედეგის დაბეჭდვა
print(f"'{str_to_count}' შეგხვდათ {count}-ჯერ ტექსტში.")
