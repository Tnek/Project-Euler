#!/usr/bin/python
n = [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 ]
temp = count = 0
x = 146
ans = 145
while True:
    for i in range(len(str(x))):
        temp += n[int(str(x)[i])]
    if temp == x:
        ans += x
        print(ans)
        break
    else:
        temp = 0
    count += 1
    x += 1
