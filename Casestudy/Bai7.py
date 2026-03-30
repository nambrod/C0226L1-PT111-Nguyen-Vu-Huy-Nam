def cahai(x):
    chuoi = [str(a) for a in x.split(",")]
    chu = 0
    so = 0
    for i in range(len(chuoi)):
        if chuoi[i].isdigit() == True:
            so += 1
        else:
            chu += 1
    if so == len(chuoi):
        print(1)
    elif chu == len(chuoi):
        print(0)
    else:
        print(-1)
a = input()
cahai(a)
