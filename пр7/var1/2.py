def summa(n):
    return sum(n)

def srzn(m):
    return (sum(m)/len(m))


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


print('Сумма элементов первого массива:', summa(a), '. Среднеарифметическое значение первого массива:', srzn(a))
print('Сумма элементов второго массива:', summa(b), '. Среднеарифметическое значение второго массива:', srzn(b))
print('Сумма элементов третьего массива:', sum(c), '. Среднеарифметическое значение третьего массива:', srzn(c))