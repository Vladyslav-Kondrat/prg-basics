def f(n):
    a = 0
    b = 1
    numberOfElement = 3
    sum_of_el = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    while numberOfElement <= n:
        c = a + b
        a = b
        b = c
        numberOfElement += 1
        sum_of_el += c
    return sum_of_el
    
print(f(5))