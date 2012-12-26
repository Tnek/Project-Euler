#!/usr/bin/python
import time
start = time.time()
import math
n = 1000000; temp = [False] * 2 + [True] * n
for i in range(2, int(math.sqrt(n))+2):
    if temp[i]:
        for j in range(i**2, n+1, i): temp[j] = False
plist = [i for i in range(len(temp)) if temp[i] if not any(int(j) % 2 == 0 or int(j) % 5 == 0 for j in str(i))]
rotate = lambda x: int(str(x)[-1] + str(x)[:-1])
def circu_check(n):
    for i in range(len(str(n)) - 1):
        n = rotate(n)
        if not n in plist: return False
    return True
print(len([i for i in plist if circu_check(i)])+2)
print(time.time() - start)
