def f(n):
    i = 0
    number_line = ""
    for i in range (1, n):
        number_line += str(i)
    return number_line


print(f(10))