def manual_len(my_list):
    length = 0
    for _ in my_list:
        length += 1
    return length

# ფუნქციის გამოძახება
my_list = [1, 2, 3, 4, 5]
print(f"სიის სიგრძე: {manual_len(my_list)}")  # შედეგი: 5

# სხვა მაგალითები:
list1 = ["ა", "ბ", "გ"]
print(f"სიის სიგრძე: {manual_len(list1)}")  # შედეგი: 3

list2 = []
print(f"სიის სიგრძე: {manual_len(list2)}")  # შედეგი: 0

list3 = [True, False, True, False, True]
print(f"სიის სიგრძე: {manual_len(list3)}")  # შედეგი: 5

list4 = [42]
print(f"სიის სიგრძე: {manual_len(list4)}")  # შედეგი: 1
