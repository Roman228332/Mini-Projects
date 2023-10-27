s = [1, 2, 3, 4, 5]
summ = 0 
for i in range(len(s)):
    if i%2==0:
       summ+=s[i]
print(s, summ)