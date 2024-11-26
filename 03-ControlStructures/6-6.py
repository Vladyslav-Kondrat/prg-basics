parking_fee = 0
hours = 2

if 1 <= hours <= 2:
    parking_fee = 5
    print(f"The fee is {parking_fee} PLN")
elif 3 <= hours <= 6:
    parking_fee = 15
    print(f"The fee os {parking_fee} PLN")
elif hours > 6:
    parking_fee = 20
    print(f"The fee is {parking_fee} PLN")