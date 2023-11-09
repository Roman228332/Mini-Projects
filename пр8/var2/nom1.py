N = 3
A = [
[2, 7, 6],
[9, 5, 1],
[4, 3, 8]]
s = 0
for i in range(N):
    s += A[0][i]
b = "да является"
for i in range(N):
    s1 = 0
    s2 = 0
    for j in range(N):
        s1 += A[i][j]
        s2 += A[j][i]
    if s1 != s or s2 != s:
        b = "нет не является"
        break
print(b)