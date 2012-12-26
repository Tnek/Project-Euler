#!/usr/bin/python
import math
pan = lambda x: sorted(list(x)) == list("123456789"[:len(x)])
prime = lambda x: not any(x%i==0 for i in range(3, int(math.sqrt(x))+2,2))
x = 7654321
while not pan(str(x)) or not prime(x): x -= 2
print(x)
