def remove_elements_by_indexes(main_list, indexes_list):
    indexes_list.sort(reverse=True)  
    for index in indexes_list:
        if 0 <= index < len(main_list):  
            main_list.pop(index)
    return main_list
