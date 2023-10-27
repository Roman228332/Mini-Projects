m = list(map(int, input().split()))
a = []
for x in m:
    if (int(x))%2==0:
        a.append(x)
print(max(a))