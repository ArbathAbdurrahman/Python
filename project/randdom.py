import random

kelas = ['a','b','c','d','e','f']
  
anggota = random.sample(kelas, k=6)
print(anggota)
nilai = 2
k1 = anggota[:nilai]
k2 = anggota[nilai:]
k3 = [4,5]

print("kelompok ", k1)
print("kelompok ", k2)
