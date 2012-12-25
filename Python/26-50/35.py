#!/usr/bin/python
import math
def prime_check(x):
    if x == 2: return True
    if x % 2 == 0 or x < 2: return False
    return not any(x % i == 0 for i in range(2, int(math.sqrt(x)) + 2))
plist = []
for i in range(1000000): 
    if prime_check(i) == True: plist.append(i)

rotate = lambda x: int(str(x)[1:] + str(x)[0])
def circu_check(n):
    for i in range(len(str(n)) - 1):
        if len(str(rotate(n))) != len(str(n)): return False
        n = rotate(n)
        if not prime_check(n): return False
    return True

clist = [i for i in plist if circu_check(i)]
for i in clist:
    if clist.count(i) > 1:
        for j in range(clist.count(i) - 1): clist.remove(i)
print(len(clist))
