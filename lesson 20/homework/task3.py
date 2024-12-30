# Input: Taking the score from the user
score = float(input("Enter the score (0-100): "))

# Determine the grade based on the score
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score"  # Handle scores outside the 0-100 range

# Output: Print the grade
print(f"The grade is: {grade}")
