a = input("Nhập số a: ")
b = input("Nhập số b: ")
try:
    print("Kết quả: ", float(a)/float(b))
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ")
except TypeError:
    print("Lỗi: Vui lòng nhập số hợp lệ")