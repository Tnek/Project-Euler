#!/usr/bin/python
import math
def prime_check(x):
    if x == 2: return True
    if x % 2 == 0: return False
    return not any(x % i == 0 for i in range(2, int(math.sqrt(x))+2))
count = 0 ; x = 2 ; plist = []
while count <= 10001:
    if prime_check(x):
        plist.append(x)
        count += 1
    x += 1
print(plist[10000])
