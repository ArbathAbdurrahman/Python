x = "udin"
y =  "demonlord"
nama = x + y
print(nama)

panjang = len(nama)
print("panjang : "+ str(panjang))

o = "o"
status = o in nama #bisa juga not in
print("ada huruf :"+ o +'='+ str(status),"di string")

#indexing (perhitungan dimulai dari 0)
print("index ke-0 :"+ nama[0])
print("index ke-6 :"+ nama[6])
print("index ke(-3) :"+ nama[-3]) #dihitung dari belakang
print("index ke(0:4) :"+ nama[0:4]) #range 0 sampai 4
print("index ke(0,2,4,6,8,10,12,13) :"+ nama[0:13:2])

#item terkecil atau terbesar
print("item terkecil : " + min(nama))
print("item terbesar : " + max(nama))

asci_code = ord("d")
print("asci code dari d : " + str(asci_code))
data = 97
print("asci code dari 97 : " + chr(data))

#method
data = "susanto subroto prawiro"
jumlah = data.count('o')
print("jumlah o dari ", data, "adalah", jumlah)