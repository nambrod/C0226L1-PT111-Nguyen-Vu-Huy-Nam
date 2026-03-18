import tkinter as ve
top = ve.Tk()
top.geometry("350x215")
ve.Frame(height = 300, width = 350, bg = "lightgray", bd = 5, relief = "ridge").place(x=0, y=0)


value = {"1": "First name:",
         "2": "Last name:",
         "3": "Address Line 1:",
         "4": "Address Line 2:",
         "5": "City:",
         "6": "State/Province:",
         "7": "Postal Code:",
         "8": "Country:"
         }
for (text, value) in value.items():
    ve.Label(top, text = value, bg = "lightgrey").place(x = 95, y = int(text)*20, anchor = "e")
    ve.Entry(top, width = 40).place(x = 95, y = int(text)*20, anchor = "w")
ve.Frame(height = 35, width = 350, bg = "lightgray").place(x=0, y=180)
ve.Button(top, text = "Submit", width = 10).place(x = 250, y = 185)
ve.Button(top, text = "Clear", width = 10).place(x = 165, y = 185)
top.mainloop()