my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
print("First element:", first_element)



last_element = my_list[-1]
print("Last element:", last_element)



first_three = my_list[:3]
print("First three elements:", first_three)



my_string = "Hello, world!"
last_five = my_string[-5:]
print("Last five characters:", last_five)




reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)



every_third = my_list[::3]
print("Every third element:", every_third)



# Ensure the list has an even number of elements
my_list = [10, 20, 30, 40, 50, 60]
midpoint = len(my_list) // 2
first_half = my_list[:midpoint]
second_half = my_list[midpoint:]
print("First half:", first_half)
print("Second half:", second_half)
