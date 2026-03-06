numbers = []
for i in range(10):
    x = int(input("Nhập số nguyên: "))
    numbers.append(x)
    x = 0
b = 0
for i in range(len(numbers)):
    if numbers[i] > 10:
        b = b + numbers[i]
print("Tổng các số lớn hơn 10:", b)