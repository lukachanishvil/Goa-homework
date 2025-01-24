def insert_at_index(lst, index, item):
    lst.insert(index, item)
    return lst

my_list = [1, 2, 3, 4]
updated_list = insert_at_index(my_list, 2, 'new_item')
print(updated_list)
