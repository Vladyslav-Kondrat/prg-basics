from functools import reduce

func = lambda x, y: x + y

numbers = [1, 2, 3, 4, 5]

result = reduce(func, numbers)
print(result)
