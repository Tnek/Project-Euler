#!/usr/bin/python
import math
tri = lambda x: x*(x+1)/2
d = 2
count = 0
while d <= 500:
    d = 2
    n = tri(count)
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0: d += 2
    count += 1
print(n)
