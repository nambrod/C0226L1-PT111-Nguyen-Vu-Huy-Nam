import math 
mang = input("Nhập mảng: ")
b = [int(x) for x in mang.split(",")]
print(b)
i = 0
check = 0
for i in range(len(b)//2):
    if b[i] == b[-1-i]:
        check += 1
if check >= len(b)//2:
    print("OK")
else:
    print("NO")