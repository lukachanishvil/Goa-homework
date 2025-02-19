
my_tuple = (10, 20, 30, 40, 50)


try:
    my_tuple[1] = 99  
except TypeError as e:
    print("Error:", e)

temp_list = list(my_tuple)
temp_list[1] = 99
my_tuple = tuple(temp_list)

print("Modified tuple:", my_tuple)
