matrica = [  [45, 3, 34], 
             [435, 6, 34], 
             [35, 34, 867]   ]


a = []

for x in range(len(matrica)):   #проходит по элементам матрицы по индексу 
    a.append(sum(matrica[x]))    #в список добавляется сумма подсписка


print('строка с наимеьншей суммой элементов: ', matrica[a.index(min(a))])
print('сумма элементов: ', min(a))


print('строка с наибольшей суммой элементов: ', matrica[a.index(max(a))])
print('сумма элементов: ', max(a))