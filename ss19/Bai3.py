def storage():
    data = []
    try:
        a = input("Nhập tên sinh viên: ")
        if a.isalpha() == False:
            print("Lỗi, tên phải là chuỗi") 
        b = int(input("Nhập tuổi: "))
        c = input("Nhập quê quán: ")
        if c.isalpha() == False:
            print("Lỗi, quê quán phải là chuỗi") 
        data.append([a,b,c])

    except ValueError: 
        print("Lỗi, tuổi là số nguyên")
    
    return data