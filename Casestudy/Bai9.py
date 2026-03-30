def lienke(x):
    chuoi = [int(a) for a in x.split(",")]
    if len(chuoi) % 2 == 1 or len(chuoi) < 2:
        print("Số chữ số phải là chẵn và khác 0")
    elif len(chuoi) % 2 == 0 and len(chuoi) >= 2:
        check = 0
        for i in range(int(len(chuoi)/2)):
            if chuoi[2*i] < chuoi[2*i+1]:
                check += 1
        if check == len(chuoi)/2:
            print("OK")
        else:
            print("NO")