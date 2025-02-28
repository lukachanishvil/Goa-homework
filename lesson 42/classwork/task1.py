
student_info = {
    "name": "გიორგი",
    "surname": "ქავთარაძე",
    "academy": "GOA",
    "fav-color": "ლურჯი",
    "city": "თბილისი",
    "goa-student": True,
    "age": 21,
    "fav-programming-lang": "Python"
}

# Dictionary-ის თითოეული მნიშვნელობის დაბეჭდვა
for key, value in student_info.items():
    print(f"{key}: {value}")
