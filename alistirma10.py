list=[]
    
for i in range(10000,100000):
    a = str(i)[0]
    b = str(i)[1]
    c = str(i)[2]
    d = str(i)[3]
    e = str(i)[4]

    if a==d and b==e:
        list.append(i)
    
print("5 basamaklı sayılardan {} tanesinin ilk iki rakamı ve son iki rakamı eşittir.".format(len(list)))

