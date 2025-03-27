vvod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vvod.txt")
vivod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vivod.txt", 'w')

matrica = []
for i in vvod:
    spisok = [int(x) for x in i.split()]
    matrica.append(spisok)

n = len(matrica)  # замена отрицательных элементов на 0 и положительных на 1
for i in range(n):
    for j in range(n):
        if matrica[i][j] < 0:
            matrica[i][j] = 0
        else:
            matrica[i][j] = 1

for i in range(n):
    for j in range(n):
        if j <= i:
            vivod.write(str(matrica[i][j]) + ' ')
    vivod.write('\n')

vvod.close()
vivod.close()
