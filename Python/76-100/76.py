#!/usr/bin/python
n = [1] + [0] * 100
for i in range(1, 100): 
    for j in range(i, 101): n[j] += n[j-i]
print(n[100])
