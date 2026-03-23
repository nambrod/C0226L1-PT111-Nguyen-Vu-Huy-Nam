info = []
with open("data.csv", "a") as ui:
    for i in range(5):
        a = input("Nhập tên: ")
        b = int(input("Nhập tuổi: "))
        c = input("Nhập nơi sinh: ")
        info.append([a, b, c])
        print(info)
    ui.write(str(info) + "\n")