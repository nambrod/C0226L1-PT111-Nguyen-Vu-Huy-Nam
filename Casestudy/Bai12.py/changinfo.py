import tkinter as tk
from data import student

# ===== FORM SỬA =====
def oke(page, sv, refresh):
    hop = tk.Toplevel(page)
    hop.title("Sửa học viên")

    tk.Label(hop, text="Mã học viên:").grid(row=0, column=0)
    tk.Label(hop, text=sv[0]).grid(row=0, column=1)

    tk.Label(hop, text="Tên:").grid(row=1, column=0)
    ten = tk.Entry(hop)
    ten.insert(0, sv[1])
    ten.grid(row=1, column=1)

    tk.Label(hop, text="Lớp:").grid(row=2, column=0)
    lop = tk.Entry(hop)
    lop.insert(0, sv[2])
    lop.grid(row=2, column=1)

    tk.Label(hop, text="Email:").grid(row=3, column=0)
    email = tk.Entry(hop)
    email.insert(0, sv[3])
    email.grid(row=3, column=1)

    tk.Label(hop, text="Ngày sinh:").grid(row=4, column=0)
    ngaysinh = tk.Entry(hop)
    ngaysinh.insert(0, sv[4])
    ngaysinh.grid(row=4, column=1)

    def save():
        sv[1] = ten.get()
        sv[2] = lop.get()
        sv[3] = email.get()
        sv[4] = ngaysinh.get()
        refresh()
        hop.destroy()

    tk.Button(hop, text="Lưu", command=save)\
        .grid(row=5, columnspan=2, pady=10)


# ===== NHẬP MÃ =====
def bandau(page, refresh):
    hop = tk.Toplevel(page)
    hop.title("Tìm học viên")

    tk.Label(hop, text="Nhập mã học viên:").grid(row=0, column=0)

    ma = tk.Entry(hop)
    ma.grid(row=0, column=1)

    thongbao = tk.Label(hop, text="")
    thongbao.grid(row=2, columnspan=2)

    def check():
        for sv in student:
            if sv[0] == ma.get():
                hop.destroy()
                oke(page, sv, refresh)
                return

        thongbao.config(text="Mã không tồn tại!", fg="red")

    tk.Button(hop, text="Tìm", command=check)\
        .grid(row=1, columnspan=2, pady=10)
