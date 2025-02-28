
def sum_numeric_values(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)): 
            total += value
    return total

data = {
    "a": 10,
    "b": 20,
    "c": 30.5,
    "d": "hello", 
    "e": 15
}

print("Sum of numeric values:", sum_numeric_values(data))
