#!/usr/bin/python
def convert(x):
    n = ""
    while x != 0:
        if x % 2 == 0:
            n += "0"
        else:
            n += "1"
        x = x // 2
    return n[::-1]
p = []
ans = 0
x = 1
while x < 999999:
    if str(x)[::-1] == str(x):
        p.append(x)
    x += 2
for i in p:
    temp = convert(i)
    if temp[::-1] == temp:
        ans += i
print(ans)
