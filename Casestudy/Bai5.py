def findMaxNumber(n):
    b = []
    if n < 1000 or n > 9999:
        print(-1)
    elif n >= 1000 and n <= 9999:
        for digit in str(n):
            b.append(int(digit))
        b.sort()
        c = b[3]*100 + b[2]*10 + b[1]
        print(c)