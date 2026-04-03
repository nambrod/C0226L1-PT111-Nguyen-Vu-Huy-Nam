import tkinter as tk
from data import student

def hopthoai(page, refresh):
    hop = tk.Toplevel(page)
    hop.title("Thêm học viên")

    # LABEL
    tk.Label(hop, text="Mã học viên:").grid(row=0, column=0)
    tk.Label(hop, text="Tên:").grid(row=1, column=0)
    tk.Label(hop, text="Lớp:").grid(row=2, column=0)
    tk.Label(hop, text="Email:").grid(row=3, column=0)
    tk.Label(hop, text="Ngày sinh:").grid(row=4, column=0)

    # ENTRY
    ma = tk.Entry(hop)
    ten = tk.Entry(hop)
    lop = tk.Entry(hop)
    email = tk.Entry(hop)
    ngaysinh = tk.Entry(hop)

    ma.grid(row=0, column=1)
    ten.grid(row=1, column=1)
    lop.grid(row=2, column=1)
    email.grid(row=3, column=1)
    ngaysinh.grid(row=4, column=1)

    # THÔNG BÁO
    tb = tk.Label(hop, text="")
    tb.grid(row=6, columnspan=2)

    def save():
        # kiểm tra rỗng
        if not all([ma.get(), ten.get(), lop.get(), email.get(), ngaysinh.get()]):
            tb.config(text="Nhập đầy đủ!", fg="red")
            return

        # kiểm tra trùng mã
        for s in student:
            if s[0] == ma.get():
                tb.config(text="Mã đã tồn tại!", fg="red")
                return

        # thêm
        student.append([ma.get(), ten.get(), lop.get(), email.get(), ngaysinh.get()])
        refresh()
        hop.destroy()

    tk.Button(hop, text="Lưu", command=save).grid(row=5, columnspan=2)
