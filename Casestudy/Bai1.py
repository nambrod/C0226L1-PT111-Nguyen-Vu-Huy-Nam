a = input("Nhập mảng số: ")
b = [int(x) for x in a.split(",")]
print(b)
if len(b) > 20:
    exit()
c = b.copy()
c.sort()
if c == b:
    print("OK")
else:
    print("NO")