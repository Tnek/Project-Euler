#!/usr/bin/python
import math
n = 2000000; pl = [False] * 2 + [True] * (n-1)
for i in range(2, int(math.sqrt(n))+2):
    if pl[i]:
        for j in range(i**2, n+1, i): pl[j] = False
print(sum([i for i in range(len(pl)) if pl[i]]))
