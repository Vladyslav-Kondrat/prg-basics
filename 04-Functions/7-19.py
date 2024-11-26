def is_prime_num(num):
    if num <= 1:
        return False
    for item in range(2, num):
        if num % item == 0:
            return False
    return True






def f(n):
    prime_value = 2
    prime_number = 1
    while prime_number < n:
        prime_value += 1
        if is_prime_num(prime_value):
            prime_number += 1
    return prime_value    

print(f(5))


