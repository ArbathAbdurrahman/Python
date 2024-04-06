#jumlah x pada y
data = "susanto subroto prawiro"
jumlah = data.count('o')
print("jumlah o dari ", data, "adalah", jumlah)

#huruf besar
data = "Aku"
print("kata :",data)
x = data.upper()
print("upper : " + x)
x = data.lower()
print("lower : " + x)
x = data.isupper()
print("is upper? : " + str(x))
x = data.islower()
print("is lower? : " + str(x))

#alphabet,num,desimal,space,title,dll
dataku = "aku123"
x = dataku.isalpha()
print("is alphabet? : " + str(x))
x = dataku.isalnum()
print("is semua janis? : " + str(x))
x = dataku.isdecimal()
print("is desimal? : " + str(x))
x = dataku.isspace()
print("is spasi? : " + str(x))
x = dataku.istitle()
print("is title? : " + str(x)) #huruf pertama besar

#mengecek komponen
x = "Udin Demonlord".startswith("Udin") #harus sama persis
print("start = " + str(x))
x = "Udin Demonlord".endswith("Demonlord") #harus sama persis
print("end = " + str(x))

#penggabungan komponen
list = ['aku', 'seorang', 'ultrament']
print(list)
gabung = ' tsah '.join(list)
print(gabung)
gabung = "aku tsah seorang tsah ultrament"
print(gabung.split('tsah'))

#alokasi karakter
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

center = "tengah".center(20,"=")
print("'" + center + "'")

#strip
center = center.strip("=") #menghilangkan
print("'" + center + "'")