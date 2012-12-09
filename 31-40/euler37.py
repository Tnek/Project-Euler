#!/usr/bin/python
import math
def pcheck(x):
    if x == 2: return True
    if x % 2 == 0 or x < 2: return False
    return not any(x % i == 0 for i in range(2, int(math.sqrt(x)) + 2))

def trunc(x): 
    if len(str(x)) <= 1: return False
    for i in range(1, len(str(x))+1):
        try:
            if not pcheck(int(str(x)[:i])) or not pcheck(int(str(x)[i:])):
                return False
        except Exception:
            print(x)
            print(i)
    return True

tlist = [ 97, 797, 3797 ]
x = 3799

while len(tlist) < 11:
    print(tlist)
    if trunc(x) and len(str(x)) > 1:
        for i in range(1, len(str(x))):
            tlist.append(int(str(x)[i:]))
            tlist.append(int(str(x)[:i]))
    x += 2
    for i in tlist:
        if len(str(i)) <= 1:
            tlist.remove(i)
    if x == 739399: 
        print("asdf")
        break
print(tlist)
print(sum(tlist))

