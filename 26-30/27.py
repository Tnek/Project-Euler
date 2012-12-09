#!/usr/bin/python
import math
def pcheck(x):
    if x == 2: return True
    if x % 2 == 0 or x < 2: return False
    return not any(x % i == 0 for i in range(3, int(math.sqrt(x)) + 2, 2))

plist = [i for i in range(1000) if pcheck(i)]

def quad(a, b):
    x = 1
    while plist.count(x**2 + a*x + b) != 0: x += 2
    return x
ans = [0]
for a in range(-999, 0, 2):
    for b in plist:
        if quad(a,b) > ans[0]: 
            ans = [quad(a, b), a, b]
print(ans[1] * ans[2])
