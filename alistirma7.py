list=[]

for i in range(100,1000):
    a = str(i)[0]
    b = str(i)[1]
    c = str(i)[2]

    if int(a) + int(b) == int(c) :
        list.append(i)

print(list)
print("3 basamaklı tam sayılardan {} tanesinin ilk iki rakamı toplamı son rakamına eşittir.".format(len(list)))
