print ('Введите год:')
a = int(input())
if a%4==0:
    print ('Год високосный. Количество дней в феврале: 29')
else:
    print ('Год не високосный. Количество дней в феврале: 28')
