
person_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "profession": "Software Engineer",
    "fav_language": "Python"
}

print("Keys:", person_info.keys())

print("Values:", person_info.values())

print("Key-Value Pairs:", person_info.items())

print("\nFormatted Key-Value Pairs:")
for key, value in person_info.items():
    print(f"{key}: {value}")
