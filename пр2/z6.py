import math
x = 16.55 * 10 ** (-3)
y = -2.75
z = 0.15
s = (10 * (x ** (1 / 3) + x ** (y + 2))) ** 0.5 * ((math.asin(z)) ** 2 - abs(x - y))
print(str(s)[:8])