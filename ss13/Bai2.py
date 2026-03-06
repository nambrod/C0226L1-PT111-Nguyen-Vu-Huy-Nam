numbers = []
for i in range(10):
    x = int(input("Nhập số nguyên: "))
    numbers.append(x)
    x = 0
numbers.sort()
print("Số lớn nhất:", numbers[-1])