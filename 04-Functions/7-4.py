def is_in_range():
    return x <= number <= y

x=2
y=15
number = 7
in_range = is_in_range()
if in_range:
    print(f"The number {number} is within the range <{x}, {y}>.")
else:
    print(f"The number {number} is not within the range <{x}, {y}>.")
