def manual_swapcase(input_string):
    # ცარიელი სთრინგი, სადაც დავაგროვებთ შედეგს
    result = ""
    for char in input_string:
        # ვამოწმებთ სიმბოლოს ტიპს და ვცვლით რეგისტრს
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char  # სხვა სიმბოლოები უცვლელი რჩება
    return result

# ფუნქციის ტესტი
user_input = input("შეიყვანეთ სთრინგი: ")
print("შედეგი:", manual_swapcase(user_input))
