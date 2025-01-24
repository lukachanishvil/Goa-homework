def csv_to_list(csv_string):
    return [item.strip() for item in csv_string.split(",")]

items = csv_to_list("apple, banana, cherry, date")
print(items)
