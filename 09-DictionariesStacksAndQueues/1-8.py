price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for key, value in price_list.items():
        print(f"{key} : {value}")

total = 0
for key, value in price_list.items():
    total += value

print(f"Total price of items = {total}")

for line in price_list:
      value_discount = value - 0,1 * value
      for key, value in price_list.items():
            print(f"{key} : {value_discount}")
