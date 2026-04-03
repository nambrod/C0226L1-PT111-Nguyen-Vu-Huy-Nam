import tkinter as tk
from tkinter import messagebox
from data import student

def xoa(page, refresh):
    #===== HỘP NHẬP MÃ =====
    hop = tk.Toplevel(page)
    hop.title("Xóa học viên")

    tk.Label(hop, text="Nhập mã học viên cần xóa:").grid(row=0, column=0)

    ma = tk.Entry(hop)
    ma.grid(row=0, column=1)

    def check():
        # tìm học viên
        for sv in student:
            if sv[0] == ma.get():

                # ===== HỎI XÁC NHẬN =====
                hoi = messagebox.askyesno(
                    "Xác nhận",
                    f"Bạn có chắc muốn xóa học viên {sv[1]} không?"
                )

                if hoi:
                    student.remove(sv)
                    refresh()
                    messagebox.showinfo("Thông báo", "Đã xóa thành công!")

                hop.destroy()
                return

        # ===== KHÔNG TỒN TẠI =====
        messagebox.showerror("Lỗi", "Mã học viên không tồn tại!")

    tk.Button(hop, text="Xóa", command=check)\
        .grid(row=1, columnspan=2, pady=10)
