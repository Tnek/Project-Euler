#!/usr/bin/python
count = 0
n = []
for a in range(2, 101):
    for b in range(2, 101):
        c = a**b
        n.append(c)
n.sort()
for i in n:
    temp = i
    for x in range(n.count(temp)-1):
        n.remove(temp)
print(len(n))
