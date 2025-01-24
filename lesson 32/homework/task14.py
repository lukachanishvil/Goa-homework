def insert_at_beginning(lst, item):
    lst.insert(0, item)
    return lst


my_list = [2, 3, 4]
updated_list = insert_at_beginning(my_list, 1)
print(updated_list)
