#!/usr/bin/python
x = 2
y = 1
ans = 0
a = 0
while y <= 1001**2:
    ans += y
    y += x
    a += 1
    if a == 4:
        x += 2
        a = 0
print(ans)
