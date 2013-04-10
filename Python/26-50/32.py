#!/usr/bin/python
pan = lambda x: sorted(str(x)) == list("123456789"[:len(str(x))])
val = lambda x, y: pan(int(str(x) + str(y) + str(x*y)))
un = lambda x: not any(x.count(str(i)) > 1 for i in range(1, 10))
n = set()
for i in range(2, 100):
    k = 1234
    if i > 9: k = 123
    for j in range(k, 10000/i+1):
        if un(str(i) + str(j)):
            if val(i, j):
                n.add(i*j)
print(sum(n))
