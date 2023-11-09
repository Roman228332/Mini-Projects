a = [[1, -5, 7], [-3, -1, 4], [6, 9, 2]]
for i in range(3):
    for j in range(3):
        if a[i][j] > 0:
            a[i][j] = 1
        elif a[i][j] < 0:
            a[i][j] = 0
print()
for i in range(3):
    for j in range(3):
        print(a[i][j], end=' ')
    print()