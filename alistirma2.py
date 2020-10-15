i=10000    #inf değerini float olarak aldığı ve hata verdiği için i sayısını büyük bir sayı tutarak yaklaşık pi değerini hesaplıyoruz.
toplam = 0

for n in range(1,i):
   toplam = toplam + (1 / n ** 2)

from math import sqrt

pi = sqrt(6 * toplam)
print('pi ~ ',pi )
