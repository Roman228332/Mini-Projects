m = list(map(int, input().split()))
a = []
for x in m:
    if int(x)%2==0 and int(x)<10:
        a.append(x)
if len(a)==0:
    print('Таких чисел нет')
else:
    print(a)



m = list(map(int, input().split()))
a = []
for x in m:
    if (int(x))%2==0:
        a.append(x)
print(max(a))