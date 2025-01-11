from functools import reduce
numbers = [2,4,6,3,7,5]
filtering = list(filter(lambda x: x % 2 == 0, numbers))
result = reduce(lambda x, y: x + y, filtering)
print(result)