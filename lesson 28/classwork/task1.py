def manual_index(main_string, search_string):
    """
    აბრუნებს საძიებელი სთრინგის პირველ ინდექსს მთავარ სთრინგში.
    თუ საძიებელი სთრინგი არ მოიძებნება, აბრუნებს -1.
    """
    main_length = len(main_string)
    search_length = len(search_string)
    
    # თუ საძიებელი სთრინგი ცარიელია ან მისი სიგრძე მეტია მთავარი სთრინგის სიგრძეზე
    if search_length == 0:
        return 0  # ცარიელი სტრინგის ინდექსი ყოველთვის 0-ია
    if search_length > main_length:
        return -1
    
    # მთავარი სთრინგის ყოველი სიმბოლოს შემოწმება საძიებელი სთრინგთან
    for i in range(main_length - search_length + 1):
        if main_string[i:i + search_length] == search_string:
            return i
    
    return -1

# მაგალითის გამოყენება
main = "გამარჯობა, როგორ ხარ?"
search = "როგორ"
print(manual_index(main, search))  # უნდა დააბრუნოს 10
