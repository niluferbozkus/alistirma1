i=10000
toplam = 0

for n in range(1,i):
   toplam = toplam + (1 / n ** 2)

from math import sqrt

pi = sqrt(6 * toplam)
print('pi ~ ',pi )
