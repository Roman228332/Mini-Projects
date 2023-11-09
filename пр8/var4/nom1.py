a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
s = []
for i in range(len(a)):
    s.append(sum(a[i]))
print("Строка с наибольшей суммой: ", a[s.index(max(s))])
print("Сумма элементов: ", max(s))
print("Строка с наименьшей суммой: ", a[s.index(min(s))])
print("Сумма элементов: ", min(s))
