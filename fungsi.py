def helloword():
    print("Hello World")

helloword()

#fungsi dengan input
a = int(input('a = '))
b = int(input('b = '))
def nama(a,b):
    hasil = a+b
    return hasil

print(f"{a} + {b} = {nama(a,b)}")

def nama(a,b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    pangkat = a ** b
    return tambah,kurang,kali,bagi,pangkat

k,l,m,n,o = nama(a,b)

print(f"operasi tambah = {k}")
print(f"operasi kurang = {l}")
print(f"operasi kali = {m}")
print(f"operasi bagi = {n}")
print(f"{a} pangkat {b} = {o}")

#fungsi pada list
def say_hi(listt):
    anggota = listt.copy()#agar list didak berubah
    for data in anggota:
        print(f"hallo {data}")

mahasiswa = ["nanung", "nining", "nonong"]
say_hi(mahasiswa)

