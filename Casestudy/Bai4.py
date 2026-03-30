def find(x):
    try:
        b = [int(i) for i in x.split("/") ]
        j = b[0]/b[1]
        so = int(j)
        if j == so:
            print(int(j),"/",1)
        else: 
            ucln = 1
            for i in range(1,b[0]+b[1]):
                if b[0]%i == 0 and b[1]%i == 0:
                    ucln = i
            tu = b[0]/ucln
            mau = b[1]/ucln
            print(int(tu),"/",int(mau))
    except ValueError:
        print("Không phải là phân số")
    except ZeroDivisionError:
        print("Không phải là phân số")
a = input("Nhập tham số a: ")
find(a)


