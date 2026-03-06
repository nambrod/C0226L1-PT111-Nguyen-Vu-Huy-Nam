numbers = []
for i in range(10):
    x = int(input("Nhập số nguyên: "))
    numbers.append(x)
    x = 0
extra = []
i = 0
for i in range(len(numbers)):
    if numbers[i] > 5:
        extra.append(numbers[i])
print("Có", len(extra), "số lớn hơn 5")