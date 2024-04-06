#membuat program menjadi simpel

#normal
def kuadratt(angka):
    return angka**2
print(f"Kuadrat dari 4 adalah {kuadratt(4)}")

#dengan lambda
#output = argumen:expression
kuadrat = lambda angka:angka**2
print(f"Kuadrat dari 4 adalah {kuadrat(4)}")

#bisa dengan 2 input
pangkat = lambda num,pow : num**pow
print(f"hasil dari 4 pangkat 2 adalah {pangkat(4,2)}")

# kegunaan Lambda
# Shorting list
data = ["aan","supri","nonong"]
data.sort()
print(f"urutan data adalah {data}")
#shorting data pakai panjang NORMAL
def panjang_nama(nama):
    return len(nama)
data.sort(key=panjang_nama)#akan mengurutkan data berdasarkan len
print(f"urutan data len adalah {data}")

#shorting menggunakan LAMBDA
data = ["aan","supri","nonong"]
data.sort(key=lambda nama:len(nama))
print(f"sorting menggunakan lambda {data}")

#NORMAl
dangka = [1,2,3,4,5,6,7,8]
def krdrlima(angka):
    return angka < 5
kurang_dari = list(filter(krdrlima,dangka))
print(f"kurang dari lima {kurang_dari}")

#menggunakan Lambda
kurang_darii = list(filter(lambda x:x<5, dangka))
print(f"kurang dari lima {kurang_darii} (Lambda)")

genap = list(filter(lambda x:(x%2==0), dangka))
print(f"angka genap {genap} (Lambda)")

ganjil = list(filter(lambda x:(x%2!=0), dangka))
print(f"angka gajil {ganjil} (Lambda)")


#ANONYMOUS FUNCTION
def pangkatt(angka,n):
    hasil = angka**n
    return hasil
pangkat2 = pangkatt(5,2)
print(f"hasil dari 5 pangkat 2 adalah {pangkat2}")

#anonim lambda
def pangkatn(n):
    return lambda angka:angka**n
pangkat_2 = pangkatn(2)
print(f"hasil dari 5 pangkat 2 adalah {pangkat_2(5)} (lambda)")
print(f"hasil dari 5 pangkat 2 adalah {pangkatn(2)(5)} (lambda)")