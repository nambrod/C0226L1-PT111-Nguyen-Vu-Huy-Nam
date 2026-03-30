def docfile():
    ten = input("Nhập tên file: ")
    try:
        with open(ten, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Lỗi, không tìm thấy file")
docfile()