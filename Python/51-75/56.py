#!/usr/bin/python
print(max([sum([int(i) for i in c]) for c in [str(a**b) for a in range(100) for b in range(100)]]))
