employee = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

employees_cap = list(map(lambda name: (name[0].upper()) + ", " + name[1], employee))
print(employees_cap)