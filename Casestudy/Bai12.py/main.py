import tkinter as tk
import addinfo as add
import changinfo as sua
import deleteinfo as xoa
from data import student

page = tk.Tk()
page.geometry("700x500")
page.title("Danh sách học viên")

# ===== HEADER =====
tk.Label(page, text="Mã học viên", relief="solid").grid(row=1, column=0)
tk.Label(page, text="Tên", relief="solid").grid(row=1, column=1)
tk.Label(page, text="Lớp", relief="solid").grid(row=1, column=2)
tk.Label(page, text="Email", relief="solid").grid(row=1, column=3)
tk.Label(page, text="Ngày sinh", relief="solid").grid(row=1, column=4)

# ===== HIỂN THỊ =====
def show():
    # xóa bảng cũ
    for widget in page.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.destroy()

    # vẽ lại
    for i, s in enumerate(student):
        tk.Label(page, text=s[0], relief="solid").grid(row=i+2, column=0)
        tk.Label(page, text=s[1], relief="solid").grid(row=i+2, column=1)
        tk.Label(page, text=s[2], relief="solid").grid(row=i+2, column=2)
        tk.Label(page, text=s[3], relief="solid").grid(row=i+2, column=3)
        tk.Label(page, text=s[4], relief="solid").grid(row=i+2, column=4)

# ===== BUTTON =====
tk.Button(page, text="Thêm học viên",
          command=lambda: add.hopthoai(page, show))\
          .grid(row=0, column=0, columnspan=2)

tk.Button(page, text="Sửa học viên",
          command=lambda: sua.bandau(page, show))\
          .grid(row=0, column=2, columnspan=2)

tk.Button(page, text="Xóa học viên",
          command=lambda: xoa.xoa(page, show))\
          .grid(row=0, column=4, columnspan=2)

page.mainloop()
