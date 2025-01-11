def mean(x,y):
    formula = (x + y) / 2
    return formula

n1 = int(input("Enter the first value: "))
n2 = int(input("Enter the second value: "))

result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')