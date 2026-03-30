def nguyento(x):
    chuoi = [int(a) for a in x.split(",")]
    chuoi.sort()
    nguyento = 0
    check = 0
    for i in range(len(chuoi)):
        for j in range(1, chuoi[i]+1):
            if chuoi[i] == 1:
                check = 2
            elif chuoi[i] % j == 0:
                check += 1
        if check == 2:
            nguyento += 1
        check = 0
    if nguyento == len(chuoi):
        print("True")
    else:
        print("False")
