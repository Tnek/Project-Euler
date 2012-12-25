#!/usr/bin/python
import math
def check(x):
    if x == 2:  return True
    if x < 2 or x % 2 == 0:  return False
    return not any(x % i == 0 for i in range(3, int(math.sqrt(x)) + 1, 2))
print(sum([i for i in range(2, 2000000) if check(i)]))
