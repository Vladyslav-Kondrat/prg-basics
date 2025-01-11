n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


mean = lambda x, y: (x + y) / 2

result = mean(n1,n2)
print(f"The arithmetic mean is {result}")