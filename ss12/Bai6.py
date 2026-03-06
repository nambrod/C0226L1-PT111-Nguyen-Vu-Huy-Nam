import password_utils as pu
a = input("Nhập mật khẩu từ bàn phím: ")
if pu.is_strong_password(a) == True:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")