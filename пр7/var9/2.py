import math
print('Введите 3 массива чисел:')
a = [int(p) for p in input().split()]
b = [int(l) for l in input().split()]
c = [int(f) for f in input().split()]
print('Произведение 1 массива:', math.prod(a),' Среднее арифметическое 1 массива:', sum(a)/len(a))
print('Произведение 2 массива:', math.prod(b),' Среднее арифметическое 2 массива:', sum(b)/len(b))
print('Произведение 3 массива:', math.prod(c),' Среднее арифметическое 3 массива:', sum(c)/len(c))