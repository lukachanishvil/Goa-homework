# პირველი რიცხვის შეყვანა და მთელ რიცხვად გარდაქმნა
start = int(input("შეიყვანეთ საწყისი რიცხვი: "))

# მეორე რიცხვის შეყვანა და მთელ რიცხვად გარდაქმნა
end = int(input("შეიყვანეთ საბოლოო რიცხვი: "))

# ციკლი დიაპაზონზე
for i in range(start, end + 1):  # end + 1, რადგან range() ბოლო რიცხვს არ შეიცავს
    square = i ** 2
    sum_with_start = i + start
    sum_with_end = i + end
    prod_with_start = i * start
    prod_with_end = i * end
    
    print(f"{i}-ის კვადრატი: {square}")
    print(f"{i}-ის და პირველი რიცხვის ჯამი: {sum_with_start}")
    print(f"{i}-ის და მეორე რიცხვის ჯამი: {sum_with_end}")
    print(f"{i}-ის და პირველი რიცხვის ნამრავლი: {prod_with_start}")
    print(f"{i}-ის და მეორე რიცხვის ნამრავლი: {prod_with_end}")
    print("---")
