list=[]

x= " "

for i in range(1,10):

    if i < 9 :
        list.append(i)

for i in range(10,100):
    a = str(i)[0]
    b = str(i)[1]
   
    if int(a) + int(b) < 9 :
        list.append(i)

for i in range(100,1000):
    a = str(i)[0]
    b = str(i)[1]
    c = str(i)[2]

    if int(a) + int(b) + int(c) < 9 :
        list.append(i)

print(*list,sep=" ")
