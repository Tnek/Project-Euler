#!/usr/bin/python
import math
def pan_check(x): return sorted(list(str(x))) == list("123456789"[:len(str(x))])
def pcheck(x): return not any(x % i == 0 for i in range(3, int(math.sqrt(x)) + 2, 2))
x = 7654321
while not pan_check(x) or not pcheck(x): x -= 2
print(x)
