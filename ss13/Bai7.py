def menu():
    print("----------Chương trình quản lý bạn bè trên Facebook--------------")
    print("Nhập phím 1 để hiển thị danh sách bạn bè")
    print("Nhập phím 2 để thêm mới bạn bè")
    print("Nhập phím 3 để xóa bạn bè")
    print("Nhập phím 4 để sửa tên bạn bè")
    print("Nhập phím 5 để thoát chương trình")
namelist = []
def phim1():
    print("\n")
    print(namelist)
def phim2():
    print("\n")
    x = input("Thêm tên mới: ")
    namelist.append(x)
def phim3():
    print("\n")
    y = input("Xóa tên bạn bè: ")
    namelist.pop(y)
def phim4():
    print("\n")
    a = input("Nhập tên muốn sửa: ")
    b = input("Nhập tên mới: ")
    c = namelist.index(a)
    namelist.pop(c)
    namelist.append(b)
    namelist.sort()
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
        break
  