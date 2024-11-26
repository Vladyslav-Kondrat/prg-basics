def amount_to_pay(amount):
    coins5 = 0
    coins2 = 0
    coins1 = 0
    if amount >= 5:
        coins5 = amount // 5
        amount  = amount % 5
    if amount >= 2:
        coins2 = amount // 2
        coins1 = amount % 2
    NumberOfCoins = coins5 + coins2 + coins1
    return NumberOfCoins

print(amount_to_pay(23))

