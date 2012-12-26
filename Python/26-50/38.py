#!/usr/bin/python
def pan(x): return sorted(list(str(x))) == list("123456789")
print(max([str(x) + str(x*2) for x in range(9876) if pan(int(str(x) + str(x*2)))])) 
