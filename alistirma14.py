#Çarpımları 121212 olan iki sayıdan farkları en küçük olanları yazdıran konsol program:



i_liste=[]
j_liste=[]
for i in range(100,10000):           #Sayıların çarpımı 6 basamaklı olması ve sayıların
    for j in range(i,10000):         #birbirine yakın olması için en az 3 en fazla 4 basamaklı sayılar alabiliriz
        if i*j==121212:          
            i_liste.append(i)
            j_liste.append(j)
print(max(i_liste),min(j_liste))
