def f(x, y):
    all_numbers = 0
    for number in range (x, y + 1):
        if number < 0 and number % 2 == 0:
            all_numbers += 1
    return(all_numbers)
print(f(-7, 8))