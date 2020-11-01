list=[]

for i in range(100,1000):
    a = str(i)[0]
    b = str(i)[1]
    c = str(i)[2]

    if i %2 == 0: 
        if a==b :
            list.append(i)
        elif a==c :
            list.append(i)
        elif b==c :
            list.append(i)

        
print("3 basamaklı çift sayılardan {} tanesinin en az iki rakamı eşittir.".format(len(list)))

