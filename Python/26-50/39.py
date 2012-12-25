#!/usr/bin/python
b = lambda a, p: (p**2 - 2*p*a) / (2*p - 2*a)
f = lambda p: len([True for a in range(int(p/2)) if b(a, p) == int(b(a, p))])
temp = [0, 0]
for p in range(1000):
    if temp[0] < f(p):
        temp[0] = f(p); temp[1] = p
print(temp[1])
