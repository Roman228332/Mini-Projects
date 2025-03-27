def summa_polozh_elementov(A):    #А - матрица
    n = len(A)      #расчет количества строк
    sum_polozhit = 0
    kolvo_polozhit = 0    #счетчики
    
    for i in range(n):     #перебор строк
        for j in range(i + 1, n):      #перебор столбцов с ай+1 чтобы обрабатывались элементы выше глав диагонали
            if A[i][j] > 0:               #если эелемент положительный то
                sum_polozhit += A[i][j]      #к сумме прибавляется величина элмента
                kolvo_polozhit += 1          #+1 к количеству
                
    return sum_polozhit, kolvo_polozhit     #возвращает сумму и кол-во



matrica = [  [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]   ]

sum_polozhit, kolvo_polozhit = summa_polozh_elementov(matrica)
print("сумма положительных элементов:", sum_polozhit)
print("кол-во положительных элементов:", kolvo_polozhit)
