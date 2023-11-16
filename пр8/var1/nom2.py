def smena_mestami_elementov(matrica):
    for stroka in matrica:
        min_index = stroka.index(min(stroka))   #индекс мин элемента в строке
        max_index = stroka.index(max(stroka))      #индекс макс элемента в строке
        stroka[0], stroka[min_index] = stroka[min_index], stroka[0]          #первый элемент меняются с минимальным
        stroka[-1], stroka[max_index] = stroka[max_index], stroka[-1]        #второй элемент меняются с максимальным
    return matrica

A = [ [7, 5, 8],
      [5, 4, 9],
      [3, 6, 1]  ]

resultat = smena_mestami_elementov(A)
print(resultat)