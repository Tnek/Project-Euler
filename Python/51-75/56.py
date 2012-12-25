#!/usr/bin/python
s = 0
ans = 0
for a in range(100):
    for b in range(100):
        c = str(a**b)
        for x in range(len(c)):
            s += int(c[x])
        if s > ans:
            ans = s
        s = 0
print(ans)
