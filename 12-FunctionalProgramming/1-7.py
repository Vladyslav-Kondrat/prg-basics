number = int(input("Enter your number: "))
is_even = ((lambda x, y: x % y)(number, 2))
if is_even == 0:
    print("Even")
else:
    print("Not even")