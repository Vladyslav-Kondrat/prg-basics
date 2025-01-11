name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
initials = (lambda x, y: x[0] + y[0])(name, surname)
print(initials)