i = 10000
toplam = 1
carpim = 1

for n in range(0,i):
    carpim *= n+1
    toplam += (1/carpim)

print('e ~ ', toplam)
