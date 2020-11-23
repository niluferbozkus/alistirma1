for year in range(1900,2005):    #Döngü daha fazla uzamasın diye rastgele olarak 1900 verdim.
    if int(str(year)[0])+int(str(year)[1])+int(str(year)[2])+int(str(year)[3]) == 2005 - year:
        print(f"{year} yılında doğmuştur.")
