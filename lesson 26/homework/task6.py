def factorial(n):
    if n < 0:
        raise ValueError("ფაქტორიალი არ გამოითვლება უარყოფითი რიცხვებისთვის")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# ფუნქციის გამოძახების მაგალითები:
print(factorial(5))  # შედეგი: 120
print(factorial(0))  # შედეგი: 1
print(factorial(1))  # შედეგი: 1
print(factorial(7))  # შედეგი: 5040
