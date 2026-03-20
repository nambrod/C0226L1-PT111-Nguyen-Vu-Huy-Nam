import tkinter as tk
page = tk.Tk()
page.geometry("500x300")
page.title("Nhập tên")
tk.Label(page, text = "Tên của bạn:", font = (15)).place(relx = 0.1, rely = 0.4)
entry = tk.Entry(page, width = 40)
entry.place(relx = 0.37, rely = 0.42)
ok = tk.Button(page, text = "Đăng nhập")
ok.place(relx = 0.37, rely = 0.5)  
def danhap(event):
    hihi = entry.get()
    tk.Label(page, text = "Tên bạn đã nhập là: " + hihi, font = (15)).place(relx = 0.1, rely = 0.3)
ok.bind("<Button-1>", danhap)
page.mainloop()