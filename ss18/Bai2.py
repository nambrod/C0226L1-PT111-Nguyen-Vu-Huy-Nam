import tkinter as tk
page = tk.Tk()
page.title("Form đăng ký khuyến mãi")
page.geometry("500x500")
page.configure(bg="black")
tk.Label(page, text = "ĐĂNG KÝ NHẬN KHUYẾN MÃI", font = ("Arial", 15)).place(relx = 0.5, rely = 0.1, anchor = "center")
info = ["Họ và tên", "Số điện thoại", "Email", "Ngày sinh"]
store = []
data = []

for i in range(4):
    tk.Label(page, text = info[i], font = ("Arial", 12)).place(x = 20, y = 100 + i * 50)
for i in range(3):
    a = tk.Entry(page)
    a.place(x = 150, y = 100 + i * 50, width = 250)
    store.append(a)

day = tk.StringVar(value="Ngày")
month = tk.StringVar(value="Tháng")
year = tk.StringVar(value="Năm")

tk.OptionMenu(page, day, *range(1, 32)).place(x = 155, y = 250, width = 65)
tk.OptionMenu(page, month, *range(1, 13)).place(x = 235, y = 250, width = 65)
tk.OptionMenu(page, year, *range(1980, 2026)).place(x = 315, y = 250, width = 65)



def oke(event):
    birth = [day.get(), month.get(), year.get()]
    data = [store[0].get(), store[1].get(), store[2].get(), day.get(), month.get(), year.get()]
    if "" in data :
        tk.Label(page, text = "Vui lòng điền đầy đủ thông tin", font = ("Arial", 12), fg = "red").place(relx = 0.5, rely = 0.9, anchor = "center")
    else:
        with open("khuyenmai.csv", "a") as ui:
            ui.write(str(data) + "," + "\n")

submit = tk.Button(page, text = "Đăng ký nhận khuyến mãi", font = ("Arial", 12), bg = "gray", fg = "white")
submit.place(relx = 0.5, rely = 0.7, anchor = "center")
submit.bind("<Button-1>", oke)
page.mainloop()