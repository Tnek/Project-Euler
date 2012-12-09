#!/usr/bin/python
print(min([i for i in range(1, 251748) if all(sorted(list(str(i*j))) == sorted(list(str(i))) for j in range(2, 7))]))
