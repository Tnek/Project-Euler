#!/usr/bin/python
import itertools
for i in [i for i in itertools.permutations('0123456789', 10)][1000000]: print(i, end="")
