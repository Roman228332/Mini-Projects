s = list(map(int, input().split()))

for i in range(len(s)):
    if s[i] < 15:
        s[i] = s[i]*2 
print(s)