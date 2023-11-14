def prostota(n, delitel=2):
    if n <= 1:
        return False
    if n % delitel == 0:
        return False
    
    if delitel * delitel > n:
        return True
    return prostota(n, delitel + 1)

chislo = int(input("Введите число для проверки на простоту: "))
if prostota(chislo):
    print("YES")
else:
    print("NO")