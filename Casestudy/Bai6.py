def songuyen(x):
    chuoi = [int(a) for a in x.split(",")]
    chan = 0
    le = 0
    for i in range(len(chuoi)):
        if chuoi[i] % 2 == 0:
            chan += 1
        if chuoi[i] % 2 == 1:
            le += 1
    if chan == len(chuoi):
        print(1)
    elif le == len(chuoi):
        print(0)
    else:
        print(-1)


