
def pryam(dlina, shirina):
    return dlina * shirina


def pryamtreug(firstkatet, secondkatet):
    return 0.5 * firstkatet * secondkatet

def trapez(firstosn, secondosn, vysota):
    return 0.5 * (firstosn + secondosn) * vysota

a = int(input('Длина прямоугольника: '))
b = int(input('Ширина прямоугольника: '))
print(pryam(a,b))

p = int(input('Первый катет: '))
o = int(input('Второй катет: '))
print(pryamtreug(p, o))

j = int(input('Первое основание: '))
h = int(input('Второе основание: '))
q = int(input('Высота: '))
print(trapez(j, h, q))