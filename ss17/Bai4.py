import tkinter as tk
import math

# Tạo cửa sổ
root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")

# Biến lưu biểu thức
expression = ""

# Hiển thị
display = tk.Entry(root, font=("Arial", 18), bd=5, relief="sunken", justify="right")
display.pack(fill="both", ipadx=8, ipady=15, padx=5, pady=5)

# Hàm xử lý
def press(key):
    global expression
    expression += str(key)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def power():
    global expression
    try:
        base, exp = expression.split("^")
        result = str(float(base) ** float(exp))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# Frame chứa nút
frame = tk.Frame(root)
frame.pack()

# Danh sách nút
buttons = [
    ("C", clear), ("√", sqrt), ("^", lambda: press("^")), ("%", lambda: press("%")),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+")),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-")),
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("*", lambda: press("*")),
    ("0", lambda: press("0")), (".", lambda: press(".")), ("=", equal), ("/", lambda: press("/")),
]

# Tạo nút dạng lưới
row = 0
col = 0

for (text, func) in buttons:
    btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14), command=func)
    
    # Nút "=" màu khác
    if text == "=":
        btn.config(bg="orange")
    
    btn.grid(row=row, column=col, padx=3, pady=3)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Chạy chương trình
root.mainloop()
