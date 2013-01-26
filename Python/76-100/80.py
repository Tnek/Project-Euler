#!/usr/bin/python
from decimal import*
getcontext().prec=102
print(sum(sum(int(j)for j in str(int(Decimal(i).sqrt()*10**99)))for i in range(2,100)if not i in{i**2 for i in range(2,10)}))
