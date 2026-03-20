import tkinter as tk
top = tk.Tk()
top.geometry("350x500")
tk.Frame(height = 200, width = 350, bg = "lightgray", bd = 5, relief = "ridge").place(x=0, y=0)


value = ["First name:",
         "Last name:",
         "Address Line 1:",
         "Address Line 2:",
         "City:",
         "State/Province:",
         "Postal Code:",
         "Country:"
]
detail = []
relabels = []
for i in range(8):
    tk.Label(top, text = value[i], bg = "lightgrey").place(x = 95, y = (i+1)*20, anchor = "e")
    info = tk.Entry(top, width = 40)
    info.place(x = 95, y = (i+1)*20, anchor = "w")
    detail.append(info)
tk.Frame(height = 35, width = 350, bg = "lightgray"). place(x=0, y=180)
sub = tk.Button(top, text = "Submit", width = 10)
sub.place(x = 250, y = 185)
def clearall(event) :
    for entry in detail:
        entry.delete(0, tk.END)
    for label in relabels:
        label.destroy()
    relabels.clear()

def submit(event):
    i = 0
    data = []
    for label in relabels:
        label.destroy()
    relabels.clear()
    for entry in detail:
        data.append(entry.get())
    for i in range(8):
        a = tk.Label(top, text = value[i] + data[i], font = ("Arial", 10))
        a.place(x = 20, y = 250+i*20)
        relabels.append(a)
clear = tk.Button(top, text = "Clear", width = 10)
clear.place(x = 165, y = 185)
clear.bind("<Button-1>", clearall)
sub.bind("<Button-1>", submit)

top.mainloop()