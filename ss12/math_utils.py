def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def is_even(a):
    if a % 2 == 0:
        return True
def is_odd(a):
    if (a % 2) == 1:
        return True
def is_prime(a):
    b = 1
    count = 0
    while a >= b:
        if a % b == 0:
            count += 1
        b += 1
    if count == 2:
        return True