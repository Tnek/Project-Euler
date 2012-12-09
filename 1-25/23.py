#!/usr/bin/python
from math import sqrt
def div(x):
    ans = 1
    if int(sqrt(x)) == sqrt(x): ans -= sqrt(x)
    return ans + sum([j for i in [[i, x//i] for i in range(2, int(sqrt(x)) + 1) if x % i == 0] for j in i])
alist = set() ; ans = 0
for i in range(1, 20162):
    if div(i) > i: alist.add(i)
    if not any((i-j in alist) for j in alist): ans += i
print(ans)
