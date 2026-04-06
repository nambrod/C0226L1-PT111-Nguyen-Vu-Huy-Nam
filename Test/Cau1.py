a = input("Nhập dãy số nguyên cách nhau bằng dấu phẩy: ")
chuoi = [int(x) for x in a.split(",")]
print(chuoi)
if len(chuoi) > 10:
    print("Dãy số có nhiều hơn 10 phần tử")
else:
    print("Dãy số có 10 phần tử hoặc ít hơn")
    check = False
    for i in range(1, len(chuoi)-1):
        if (chuoi[i] < chuoi[i-1] and chuoi[i] < chuoi[i+1]) or (chuoi[i] > chuoi[i-1] and chuoi[i] > chuoi[i+1]):
            check = True
        else:
            check = False
            print("False")
            break
    if check == True:
        print("True")