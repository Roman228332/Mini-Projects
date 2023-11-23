vvod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vvod.txt")
vivod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vivod.txt", 'w')

matrica = []
for i in vvod:
    spisok = [int(x) for x in i.split()]
    matrica.append(spisok)

a = []
for x in range(len(matrica)):  # проходит по элементам матрицы по индексу
    a.append(sum(matrica[x]))  # в список добавляется сумма подсписка

vivod.write(f'{str(matrica[a.index(min(a))])}' + '\n')
vivod.write(f'{str(min(a))}' + '\n')

vivod.write(f'{str(matrica[a.index(max(a))])}' + '\n')
vivod.write(f'{str(max(a))}' + '\n')
