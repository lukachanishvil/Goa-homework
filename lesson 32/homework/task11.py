def append_multiple_to_list(lst, items):
    lst.extend(items)
    return lst


my_list = [1, 2, 3]
new_items = [4, 5, 6]
updated_list = append_multiple_to_list(my_list, new_items)
print(updated_list)
