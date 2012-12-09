#!/usr/bin/python
temp = 0
ans = 0
for x in range(2, 354294):
    for y in range(len(str(x))):
        temp += int(str(x)[y])**5
    if temp == x:
        ans += x
    temp = 0
print(ans)
