dict = {}
def menu():
    print("----------Chương trình quản lý quốc gia và thủ đô--------------")
    print("Nhập phím 1 để hiển thị danh sách quốc gia và thủ đô")
    print("Nhập phím 2 để thêm mới quốc gia và thủ đô")
    print("Nhập phím 3 để xóa quốc gia và thủ đô ")
    print("Nhập phím 4 để sửa tên thủ đô")
    print("Nhập phím 5 để tra cứu thủ đô")
    print("Nhập phím 6 để thoát chương trình")
    print("Nhập vào sự lựa chọn của bạn")
def phim1():
    print("\n")
    print(dict)
def phim2():
    print("\n")
    x = input("Nhập tên quốc gia: ")
    y = input("Nhập tên thủ đô: ")
    dict[x] = y
def phim3():
    print("\n")
    x = input("Nhập tên quốc gia cần xóa: ")
    del dict[x]
def phim4():
    print("\n")
    x = input("Nhập tên quốc gia cần sửa thủ đô: ")
    y = input("Nhập tên thủ đô mới: ")
    dict[x] = y
def phim5():
    print("\n")
    x = input("Nhập tên quốc gia cần tra cứu thủ đô: ")
    print("Thủ đô của", x, "là:", dict.get(x))
def phim6():
    print("Thoát chương trình")
i = 1
while i > 0:
    menu()
    a = int(input("Nhập phím: "))
    if a == 1:
        phim1()
    if a == 2:
        phim2()
    if a == 3:
        phim3()
    if a == 4:
        phim4()
    if a == 5:
        phim5()
    if a == 6:
        phim6()
        break
