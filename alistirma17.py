sayi = input("Palindromik olduğunu kontrol etmek istediğiniz 3 veya 4 basamaklı sayıyı girin: ")

if int(sayi)<100 or int(sayi)>=10000:
    print("Girdiğiniz sayının 3 ve 4 basamaklı olduğunu kontrol edin. ")
    sayi = input("Palindromik olduğunu kontrol etmek istediğiniz 3 veya 4 basamaklı sayıyı girin: ")
    
if int(sayi)<1000:
    if sayi[0]==sayi[2]:
        print(f"Girdiğiniz {sayi} sayısı palindromiktir.")
    else :
        print(f"Girdiğiniz {sayi} sayısı palindromik değildir.")

elif int(sayi) < 10000:
    if sayi[0]==sayi[3] and sayi[1]==sayi[2]:
        print(f"Girdiğiniz {sayi} sayısı palindromiktir.")
    else :
        print(f"Girdiğiniz {sayi} sayısı palindromik değildir.")

