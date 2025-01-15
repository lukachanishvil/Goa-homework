def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

# ფუნქციის გამოძახების მაგალითები:
print(even_or_odd(10))  # შედეგი: ლუწი
print(even_or_odd(15))  # შედეგი: კენტი
print(even_or_odd(0))   # შედეგი: ლუწი
print(even_or_odd(-4))  # შედეგი: ლუწი
print(even_or_odd(-7))  # შედეგი: კენტი
