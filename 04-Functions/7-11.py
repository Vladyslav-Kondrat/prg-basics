def f(n):
    line = "*"
    while n > 1:
        line += "/*"
        n -= 1
    return line
    
print(f(10))