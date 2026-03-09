t = (1, 2, 2, 3, 2, 4, 5)
def lan():
    a = int(input("Tìm số: "))
    print(a, "lặp", t.count(a), "lần")
lan()
def vitri():
    a = int(input("Tìm số: "))
    print("Vị trí của", a, "là", t.index(a))
vitri()