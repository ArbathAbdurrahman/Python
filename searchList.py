angka = (1,3,4,2,5,7,5,6,6,7,8,6,4,5,6,7,8,)
print(f"angka : \n{angka}")

#count data
jumlah6 = angka.count(6)
print(f"jumlah angka 6 adalah : {jumlah6}")

#mengurutkan data
my_list = [4, 2, 8, 1, 7]
my_list.sort()
print(my_list)
sort = sorted(angka)#dengan copy
dcd = sorted(angka,reverse=True)
print(f"sort \n {sort}\n dcd \n {dcd}")
kendaraan = ['motor', 'angkot', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

#mengambil data
idx = angka.index(8)
print(angka)
print(f"angka 8 ada di index ke-{idx}")

#cara mengcopy list
a = kendaraan.copy()
print(f"a={hex(id(a))}")
print(f"kendaraan={hex(id(kendaraan))}")
print(f"angka={hex(id(angka))}")

original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
# atau copied_list = list(original_list)
print(copied_list)

