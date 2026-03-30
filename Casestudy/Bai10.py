def checkString(str):
    chuoi = []
    kitu = []
    nguyenam = ["a", "e", "i", "o", "u","A","E","I","O","U"]
    for letter in str:
        chuoi.append(letter)
    for i in range(len(chuoi)-1):
        for j in range(9):
            if chuoi[i] == nguyenam[j]:
                kitu.append(chuoi[i])
    for j in range(9):
        if kitu.count(nguyenam[j]) >= 2:
            for i in range(int(kitu.count(nguyenam[j])-1)):
                kitu.remove(nguyenam[j])
    print(kitu)
