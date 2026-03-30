import math
def checkTriangle(x,y,z):
    num = []
    num.append(x)
    num.append(y)
    num.append(z)
    num.sort()
    if num[0]^2 + num[1]^2 < num[2]^2:
        print("không phải là cạnh tam giác")
    elif x < 0 or y < 0 or z < 0:
        print("không phải là cạnh tam giác")
    elif x^2 + y^2 == z^2 or x^2 + z^2 == y^2 or y^2 + x^2 == z^2:
        print("Đây là tam giác vuông")
    elif x^2 + y^2 > z^2 or x^2 + z^2 > y^2 or y^2 + x^2 > z^2:
        print("chỉ là 3 cạnh của một tam giác")