import tkinter as tk
window = tk.Tk()
window.geometry("400x250")
window.title("Login_Program")
tk.Label(window, text = "Login").place(x = 50, y = 25 )
tk.Label(window, text="Username").place(x = 50, y = 50)
rec1 = tk.Entry(window)
rec1.place(x = 50, y = 75)
tk.Label(window, text="Password").place(x = 50, y = 100)
rec2 = tk.Entry(window)
rec2.place(x = 50, y = 120)
login = tk.Button(window, text="Login")
login.place(x = 50, y = 150)
def check(event):
    if rec1.get() == "admin" and rec2.get() == "123456":
        tk.Label(window, text="Đã đăng nhập đúng").place(x = 50, y = 200)
    else: 
        tk.Label(window, text="Nhập sai mật khẩu").place(x = 50, y = 200)
login.bind("<Button-1>", check)
window.mainloop()