def find_maximum(numbers):
    if not numbers:
        raise ValueError("სია ცარიელია")
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# ფუნქციის გამოძახების მაგალითები:
print(find_maximum([3, 5, 7, 2, 8]))       # შედეგი: 8
print(find_maximum([-10, -20, -5, -7]))    # შედეგი: -5
print(find_maximum([42]))                  # შედეგი: 42
print(find_maximum([0, 0, 0]))             # შედეგი: 0
print(find_maximum([1.5, 2.5, 0.5, 2.4]))  # შედეგი: 2.5
