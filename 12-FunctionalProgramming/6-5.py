values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sorting = list(filter(lambda item: item % 2 == 0 and item % 3 == 0, values))
print(sorting)