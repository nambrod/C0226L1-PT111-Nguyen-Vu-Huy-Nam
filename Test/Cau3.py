#Taopage
import tkinter as tk
from tkinter import messagebox
page = tk.Tk()
page.title("Quản lý xe máy")
page.geometry("800x800")
stt = 0

#Button
Them = tk.Button(page, text = "Thêm xe máy")
Them.grid(row = 0, column = 0)
Xoa = tk.Button(page, text = "Xóa xe máy")
Xoa.grid(row = 0, column = 1)

#Label
List = ["Biển số xe", "Họ tên sinh viên", "Chứng minh nhân dân", "Hãng xe máy", "Phí gửi xe đã đóng"]
Tenxe = ["Honda", "Yamaha", "Sym", "Piaggio", "Suzuki", "Ducati", "Hãng khác"]
Listxe = []
for i in range(0, 5):
    tk.Label(page, text = List[i], bd = 1, relief = "solid").grid(row = 1, column = i)

#hienthi
def hienthi():
    for widget in page.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.destroy()

    for stt in range(len(Listxe)):
        for i in range(5):
            tk.Label(page, text=Listxe[stt][i]).grid(row=stt+2, column=i)

#Themxe
def hopthoai(event):
    hop = tk.Toplevel(page)
    hop.title("Thêm xe")

    # LABEL
    tk.Label(hop, text="Biển số xe:").grid(row=0, column=0)
    tk.Label(hop, text="Họ tên sinh viên:").grid(row=1, column=0)
    tk.Label(hop, text="Chứng minh nhân dân:").grid(row=2, column=0)
    tk.Label(hop, text="Hãng xe máy:").grid(row=3, column=0)
    tk.Label(hop, text="Phí gửi xe đã đóng:").grid(row=4, column=0)

    # ENTRY
    bien = tk.Entry(hop)
    ten = tk.Entry(hop)
    cmnd = tk.Entry(hop)
    hang = tk.Entry(hop)
    phi = tk.Entry(hop)

    bien.grid(row=0, column=1)
    ten.grid(row=1, column=1)
    cmnd.grid(row=2, column=1)
    hang.grid(row=3, column=1)
    phi.grid(row=4, column=1)

    # THÔNG BÁO
    tb = tk.Label(hop, text="")
    tb.grid(row=6, columnspan=2)

    def save():
        # kiểm tra rỗng
        if not all([bien.get(), ten.get(), cmnd.get(), hang.get(), phi.get()]):
            tb.config(text="Nhập đầy đủ!", fg="red")
            return

        # kiểm tra trùng biển số
        for s in Listxe:
            if s[0] == bien.get():
                tb.config(text="Biển số đã tồn tại!", fg="red")
                return
            
        #Checkhang
        for i in range(len(Tenxe)-1):
            if hang.get() == Tenxe[i]:
                pass
            else:
                tb.config(text = "Hãng xe không hợp lệ!", fg="red")

        # thêm
        if len(hang.get()) < 20 and len(ten.get()) < 40 and (cmnd.get()).isdigit() and (phi.get()).isdigit():
            Listxe.append([bien.get(), ten.get(), cmnd.get(), hang.get(), phi.get()])
            hop.destroy()
            hienthi()
            global stt
            stt += 1
        else:
            tb.config(text="Dữ liệu không hợp lệ!", fg="red")
        
    tk.Button(hop, text="Lưu", command=save).grid(row=5, columnspan=2)

#Xoaxe
def xoa(event):
    hop = tk.Toplevel(page)
    hop.title("Xóa xe máy")
    tk.Label(hop, text="Nhập biển số xe cần xóa:").grid(row=0, column=0)
    bien = tk.Entry(hop)
    bien.grid(row=0, column=1)

    def check():
        # tìm xe máy
        for xe in Listxe:
            if xe[0] == bien.get():
                hoi = messagebox.askyesno(
                    "Xác nhận",
                    f"Bạn có chắc muốn xóa xe máy {xe[0]} không?")

                if hoi:
                    Listxe.remove(xe)
                    messagebox.showinfo("Thông báo", "Đã xóa thành công!")

                hop.destroy()
                hienthi()
                return

        # ===== KHÔNG TỒN TẠI =====
        messagebox.showerror("Lỗi", "Biển số xe không tồn tại!")

    tk.Button(hop, text="Xóa", command=check)\
        .grid(row=1, columnspan=2, pady=10)


#Function
Them.bind("<Button-1>", hopthoai)
Xoa.bind("<Button-1>", xoa)
if len(Listxe) > 0:
    for stt in range(len(Listxe)):
        for i in range(5):
            tk.Label(page, text=Listxe[stt][i], bd = 1, relief = "solid").grid(row=stt+2, column=i)
page.mainloop()