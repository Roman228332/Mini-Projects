import math
a = [int(n) for n in input().split()]
b = [int(p) for p in input().split()]
c = [int(q) for q in input().split()]
sr_a = sum(a)/len(a)
sr_b = sum(b)/len(b)
sr_c = sum(c)/len(c)
sum_a = sum(a)
sum_b = sum(b)
sum_c = sum(c)
print('Сумма элементов первого массива:', sum_a, '. Среднеарифметическое значение первого массива:', sr_a)
print('Сумма элементов второго массива:', sum_b, '. Среднеарифметическое значение второго массива:', sr_b)
print('Сумма элементов третьего массива:', sum_c, '. Среднеарифметическое значение третьего массива:', sr_c)