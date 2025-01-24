def insert_at_end(lst, item):
    lst.insert(len(lst), item)  
    return lst

my_list = [1, 2, 3]
updated_list = insert_at_end(my_list, 4)
print(updated_list)
