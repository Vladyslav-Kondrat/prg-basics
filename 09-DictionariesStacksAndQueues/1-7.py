store = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for key, value in store.items():
        print(f"{key} : {value}")

total_quantity = 0
for key, value in store.items():
    total_quantity += value

print(total_quantity)