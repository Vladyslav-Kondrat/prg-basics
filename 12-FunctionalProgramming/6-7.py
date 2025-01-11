from functools import reduce
score = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

# maximum = list(map(lambda item: max(item), score))
# minimum = list(map(lambda item: min(item), score))
# func = list(filter(lambda x: max(x) and min(x), score))
# x = lambda x, y: x + y
# calculate = reduce(x, func)
# print(calculate)

total_points = list(map(lambda scores: sum(scores) - min(scores) - max(scores), score))
print(total_points)