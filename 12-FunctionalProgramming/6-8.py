grades = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
    return lambda pts: pts >= limit

num1 = list(filter(min_pts(70), grades))
print(num1)
num2 = list(filter(min_pts(40), grades))
print(num2)
num3 = list(filter(min_pts(30), grades))
print(num3)