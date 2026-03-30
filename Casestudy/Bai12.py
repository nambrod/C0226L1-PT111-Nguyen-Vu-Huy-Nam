import tkinter as tk
#Tạo page
page = tk.Tk()
page.geometry("700x500")
page.title("Danh sách học viên")

#Biến:
x = 20
y = 40
student = []

#Tạo bảng
tk.Label(page, text = "Mã học viên", relief = "solid").grid(row = 1, column = 0)
tk.Label(page, text = "Tên", relief = "solid").grid(row = 1, column = 1, padx = 20)
tk.Label(page, text = "Lớp", relief = "solid").grid(row = 1, column = 2, padx = 10)
tk.Label(page, text = "Email", relief = "solid").grid(row = 1, column = 3, padx = 20)
tk.Label(page, text = "Ngày sinh", relief = "solid").grid(row = 1, column = 4, padx = 8)

#Tạo button
new = tk.Button(page, text = "Thêm mới học viên", width = 18, height = 1, bg = "lightgray")
new.grid(row = 0, column = 0, columnspan = 2, padx = 5)
change = tk.Button(page, text = "Sửa thông tin học viên", width = 18, height = 1, bg = "lightgray")
change.grid(row = 0, column = 2, columnspan = 2, padx = 5)
delete = tk.Button(page, text = "Xóa học viên", width = 10, height = 1, bg = "lightgray")
delete.grid(row = 0, column = 4, columnspan = 2, padx = 5)

#Nhapinfo
def hopthoai():
    hop = tk.Frame(page, width = 200, height = 400, relief = "raised")
    tk.Label(hop, text = "Mã học viên", relief = "solid").grid(row = 0, column = 0)
    tk.Label(hop, text = "Tên", relief = "solid").grid(row = 0, column = 1)
    tk.Label(hop, text = "Lớp", relief = "solid").grid(row = 0, column = 2)
    tk.Label(hop, text = "Email", relief = "solid").grid(row = 0, column = 3)
    tk.Label(hop, text = "Ngày sinh", relief = "solid").grid(row = 0, column = 4)


page.mainloop()
