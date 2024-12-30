# 1. შედარება + and ოპერატორი
x = 5
y = 10
result = (x > 3) and (y < 20)
print(result)  # True, რადგან ორივე პირობა სიმართლეა

# 2. შედარება + or ოპერატორი
a = 8
b = 15
result = (a < 5) or (b > 10)
print(result)  # True, რადგან მეორე პირობა სიმართლეა

# 3. შედარება + not ოპერატორი
num1 = 7
num2 = 4
result = not (num1 == num2)
print(result)  # True, რადგან num1 და num2 არ არის თანაბარი

# 4. multiple comparisons + and
age = 25
height = 180
result = (age >= 18) and (height > 160)
print(result)  # True, ორივე პირობა სიმართლეა

# 5. multiple comparisons + or
temperature = 22
is_raining = False
result = (temperature > 20) or (is_raining)
print(result)  # True, რადგან პირველი პირობა სიმართლეა

# 6. შედარება + and + or
x = 50
y = 20
z = 100
result = (x > 30) and (y < 25) or (z == 100)
print(result)  # True, რადგან ორივე პირობა ან or-ის ნაწილი სიმართლეა

# 7. შედარება + not + or
is_adult = True
is_student = False
result = (is_adult) or not (is_student)
print(result)  # True, რადგან is_adult სიმართლეა

# 8. multiple comparisons + and + not
x = 15
y = 25
result = (x >= 10) and (y < 30) and not (x == y)
print(result)  # True, რადგან ყველა პირობა სიმართლეა

# 9. შედარება + and + or (მაგალითი ცვლადებით)
num1 = 5
num2 = 8
num3 = 12
result = (num1 < num2) and (num2 < num3) or (num1 == 5)
print(result)  # True, რადგან or-ის ნაწილი სიმართლეა

# 10. multiple comparisons + and + or (მაგალითი ბულეანებით)
is_weekend = True
is_holiday = False
has_free_time = True
result = (is_weekend and not is_holiday) or has_free_time
print(result)  # True, რადგან პირველი პირობა სიმართლეა


