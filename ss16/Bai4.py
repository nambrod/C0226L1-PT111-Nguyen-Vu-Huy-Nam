import tkinter as tk
top = tk.Tk()
top.geometry("300x400")
hang1 = ["C", "căn", "x^y", "%"]
hang2 = ["1", "2", "3"]
hang3 = ["4", "5", "6"]
hang4 = ["7", "8", "9"]
hang5 = ["0", "."]
cot1 = ["+", "-", "*", "/"]
frame1 = tk.Frame(top, height = 100, width = 300, bg = "white", bd =15, relief = "ridge")
frame1.pack(fill = "x")
entry1 = tk.Entry(frame1, width = 22, font = (100))
entry1.place(relx = 1, rely = 0.5, anchor = "e")
i = 0
while i <= 3:
    tk.Button(top, text = hang1[i], bg = "darkgray").place(x = i * 300/4, y = 100, width = 300/4, height = 300/4)
    i += 1
i = 0
while i <= 2:
    tk.Button(top, text = hang2[i], bg = "lightgray").place(x = i * 300/4, y = 100 + 300/4, width = 300/4, height = 300/4)
    i += 1
i = 0
while i <= 2:
    tk.Button(top, text = hang3[i], bg = "lightgray").place(x = i * 300/4, y = 100 + 2 * 300/4, width = 300/4, height = 300/4)
    i += 1
i = 0
while i <= 1:
    tk.Button(top, text = hang4[i], bg = "lightgray").place(x = i * 300/4, y = 100 + 3 * 300/4, width = 300/4, height = 300/4)
    i += 1
i = 0
while i <= 2:
    tk.Button(top, text = cot1[i], bg = "darkgray").place(x = 300/4*3, y = 100+300/4 + i * 300/4, width = 300/4, height = 300/4)
    i += 1
tk.Button(top, text = "=", bg = "orange").place(x = 300/4*2, y = 100+300/4 + 2 * 300/4, width = 300/4, height = 300/4)
top.mainloop()