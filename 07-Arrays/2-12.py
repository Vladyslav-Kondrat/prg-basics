

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

maximum_cost = (max(expenses))
index = expenses.index(maximum_cost)
print(categories[index])