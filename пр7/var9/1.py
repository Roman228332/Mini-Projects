def summa_cifr(n):
    r = 0
    while n > 0:
        r += (n % 10)
        n = n // 10
    return r


c = int(input("Введите число: "))
kolvo = 0
while c > 0:
    c -= summa_cifr(c)
    kolvo += 1
print(kolvo)