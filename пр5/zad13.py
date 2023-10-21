s = (input())
s = s.split("(")
s.pop(0)
g = s[0]
g = g.split(")")
print(g[0])