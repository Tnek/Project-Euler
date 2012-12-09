#!/usr/bin/python
def check(x): return len([x for i in range(11, 21) if x % i == 0]) == 10
x = 2520 
while not check(x): x += 2520
print(x)
