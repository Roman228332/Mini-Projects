def smena_mestami_elementov(matrica):
    for stroka in matrica:
        min_index = stroka.index(min(stroka))   #индекс мин элемента в строке
        max_index = stroka.index(max(stroka))      #индекс макс элемента в строке
        stroka[0], stroka[min_index] = stroka[min_index], stroka[0]          #первый элемент меняются с минимальным
        stroka[-1], stroka[max_index] = stroka[max_index], stroka[-1]        #второй элемент меняются с максимальным
    return matrica

vvod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vvod.txt")
vivod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vivod.txt", 'w')

matritsa = []
for line in vvod:
    strok = [int(x) for x in line.split()]    
    matritsa.append(strok)
vvod.close()
result = smena_mestami_elementov(matritsa)
for strok in result:    
    vivod.write(' '.join(map(str, strok)) + '\n')
vivod.close()
