iu = input("Nhập ngày tháng năm (dd/mm/yyyy): ")
def check(a):
    chuoi = [x for x in a.split("/")]
    if len(str(chuoi[0])) == 2 and len(str(chuoi[1])) == 2 and len(str(chuoi[2])) == 4:
        try:
            day = int(chuoi[0])
            month = int(chuoi[1])
            year = int(chuoi[2])
            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                pass
            else:
                print("yêu cầu nhập đúng định dạng dd/MM/yyyy")
            if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
                print(year, "là năm nhuận")
            else:
                print(year, "không phải là năm nhuận")
        except ValueError:
            print("yêu cầu nhập đúng định dạng dd/MM/yyyy")
    else:
        print("yêu cầu nhập đúng định dạng dd/MM/yyyy")
check(iu)