#!/usr/bin/python
def convert(x):
    n = ""
    while x != 0:
        n += str(x % 2); x //= 2
    return n[::-1]
p = [i for i in range(1, 999999, 2) if str(i)[::-1] == str(i)]
print(sum([i for i in p if convert(i) == convert(i)[::-1]]))
