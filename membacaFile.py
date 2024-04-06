print("="*3,"Membaca File","="*3)
file = open('data.txt',mode='r')

print(f"apakah data bisa dibaca? {file.readable()}")
print(f"apakah data bisa ditulis? {file.writable()}")

#membaca file
# print(file.read())

#membaca per baris
# print(file.readline(),end="")
# print(file.readline(),end="")

#membaca sebagai list
print(file.readlines())

#menutup file yg sedang dibaca
print(f"apakah file sudah ditutup?{file.closed}")
file.close()
print(f"apakah file sudah ditutup?{file.closed}")

#Teknik membuka file yang simple menggunakan with
print('\n',"="*3,"Membaca File menggunakan with ","="*3)

with open('data.txt',mode='r') as file:
    print(file.readline(),end='')#open data pertama
    print(f"apakah file sudah ditutup?{file.closed}")

print(f"apakah file sudah ditutup?{file.closed}") #maka akan otomatis menutup file 