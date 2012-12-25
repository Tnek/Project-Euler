#!/usr/bin/python
def div(x): return sum([i for i in range(1, x) if x % i == 0])
print(sum([i for i in range(1, 10000) if div(div(i)) == i and div(i) != i]))
