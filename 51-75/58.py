#!/usr/bin/python
import math
def pcheck(x):
    if x == 2: return True
    if x % 2 == 0 or x < 2: return False
    return not any(x % i == 0 for i in range(3, int(math.sqrt(x)) + 2, 2))

plist = [i for i in range(1000000) if pcheck(i)]
list = [int(i) for i in open("plist.txt", "r").readlines()]

x = 2
y = 1
a = 0
while y <= 1001**2:
    y += x
    a += 1
    if a == 4:
        x += 2
        a = 0

