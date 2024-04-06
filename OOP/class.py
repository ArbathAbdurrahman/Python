class Mobil: #template
    #class variabel
    jumlah = 0

    def __init__(self,color,merk,model) -> None:
        #instance variable
        self.warna = color
        self.merek = merk
        self.seri = model
        Mobil.jumlah += 1
        print("--> membuat mobil dengan merek " + merk)

import os
os.system("cls")
mobil1 = Mobil("merah","fuso",3214)
print(Mobil.jumlah)
mobil2 = Mobil("biru","ferari",8636)
print(Mobil.jumlah)
mobil3 = Mobil("hitam","mensedes",5463)
print(Mobil.jumlah)


print(mobil1.warna)
print(mobil2.seri)
print(mobil3.__dict__)