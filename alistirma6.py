list=[]

for i in range(1000,10000):
    a = str(i)[0]
    b = str(i)[3]

    if int(a) > int(b) :
        list.append(i)

print("4 basamaklı tam sayılardan {} tanesinin ilk rakamı son rakamından büyüktür.".format(len(list)))

#liste=[]
#for i in range(1000,10000):
#    if int(str(i)[0]) > int(str(i)[3]):
#        liste.append(i)
#print(len(liste))
