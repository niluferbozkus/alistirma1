sayi=int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))

if sayi<0:
    print("Asal sayılar 0'dan büyüktür!")
    asal=False
elif sayi <=1:
    asal=False
else:
    asal=True
    for i in range(2,sayi):
        if sayi % i == 0:
            asal= False         
        
if asal==True:
    print(f"{sayi} sayısı asal bir sayıdır.")
else:
    print(f"{sayi} sayısı asal değildir.")

