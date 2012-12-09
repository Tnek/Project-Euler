#!/usr/bin/python
import math
for a in range(1, 999):
    for b in range(1, 999):
        c = math.sqrt(a**2 + b**2)
        if int(c) == c and a + b + c == 1000:
            ans = a * b * c
            break
print(ans)
