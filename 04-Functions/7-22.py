def f(password):
    for char in password:
        if password.count(char) <= 1:                        #why
            return True
        else:
            return False
        
print(f("hello"))