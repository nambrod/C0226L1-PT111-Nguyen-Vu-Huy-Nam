import math_utils as ma
x = int(input("Nhập số nguyên a: "))
if ma.is_even(x) == True:
    print(x, "là số chẵn")
else:
    print(x, "không phải là số chẵn")
if ma.is_odd(x) == True:
    print(x, "là số lẻ")
else:
    print(x, "không phải là số lẻ")
if ma.is_prime(x) == True:
    print(x, "là số nguyên tố")
else:
    print(x, "không phải là số nguyên tố")
