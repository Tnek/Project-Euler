#!/usr/bin/python
def chain(x):
    count = 1
    while x != 1:
        if x % 2 == 0: x /= 2
        else: x = (x * 3) + 1
        count += 1
    return count
n = [i for i in range(500001, 1000000, 2)]
y = [chain(i) for i in range(500001, 1000000, 2)]
print(n[y.index(max(y))])
