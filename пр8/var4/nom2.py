matrica = [  [-45, 29, 13], 
             [34, -95, 46], 
             [67, 88, -19]    ]


n = len(matrica)   #замена отрицательных элементов на 0 и положительных на 1
for i in range(n):
    for j in range(n):
        if matrica[i][j] < 0:
            matrica[i][j] = 0
        else:
            matrica[i][j] = 1


for i in range(3):
    for j in range(3):
        if j <= i:
            print(matrica[i][j], end=' ')
    print()