#default argumennya "gantenk"
def sapa(nama, pesan = "gantenk"): #Position
    print(f"hallo {nama} {pesan}")

sapa("Supri","apa kabar?")
sapa("Asep")

#Bentuk-bentuk Fungsi
def tambah(*args):
    # bertipe data tuple
    output = 0
    for angka in args:
        output += angka
    return output

hasil = tambah(1,2,3,4,5)
print(f"hasil = {hasil}")


def data(**kwagrs):
    nama = kwagrs['nama']
    tinggi = kwagrs['tinggi']
    berat = kwagrs['berat']
    print(f"{nama} mempunyai tinggi {tinggi} dan berat {berat}")

data(nama="Supri",tinggi=180,berat=70)


def fungsi_gabungan(*args, **kwargs):
    # Lakukan sesuatu dengan args
    for arg in args:
        print("Argumen posisi:", arg)
    
    # Lakukan sesuatu dengan kwargs
    for key, value in kwargs.items():
        print("Argumen kata kunci:", key, "=", value)

# Contoh pemanggilan fungsi_gabungan
fungsi_gabungan(1, 2, 3, nama="John", usia=25)


def math(*args,**kwargs):
    outp = 0
    outq = 1
    if kwargs["option"]==["tambah"]:
        for angka in args:
            outp += angka
    elif kwargs["option"] == ["kali"]:
        for i in args:
            outq *= i
    else :
        print("tidak ad aopersi")
    return outq,outp

hasil1 = math(1,2,3,4,5,option="tambah")
print(f"hasil1 {hasil1}")
hasil2 = math(1,2,3,4,5,option="kali")
print(f"hasil2 {hasil2}")
    