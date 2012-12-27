#!/usr/bin/python
import math
print(max(i for i in range(3, int(math.sqrt(600851475143)) + 2, 2) if 600851475143 % i == 0 and not any(i % j == 0 for j in range(3, int(math.sqrt(i))+2, 2))))
