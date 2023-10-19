#6задание
#n = int(input('Введите число: '))
#f = 1
#for i in range(1, n+1):
#    f = f * i
#print(f)



#2задание
#a = int(input('Введите первое число: '))
#b = int(input('Введите второе число: '))
#if a<b:
#    for i in range(a, b+1):
#        print(i)
#else:
#    for x in range(a, b-1, -1):
#        print(x)



#8задание
n = int(input('Введите число: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
