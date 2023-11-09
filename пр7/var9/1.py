def f(n):
    r = 0
    while n > 0:
        r += n % 10
        n = n // 10
    return r
c = int(input("Введите число: "))
r = 0
while c > 0:
    c -= f(c)
    r += 1
print(r)