nama = "udin"
format_str = f"mana {nama}"
print(format_str)

#boolean
bool = True
format_str = f"boolean = {bool}"
print(format_str)

#angka
angka = 2004.8
format_str = f"angka = {angka}"
print(format_str)
angka = 2004
format_str = f"bilbul = {angka:d}" #jika bolangan bulat
print(format_str)
angka = 2004
format_str = f"ribuan = {angka:,}"
print(format_str)
angka = 2004.54321
format_str = f"ribuan = {angka:.3f}" #untuk mengambil 3 angka dibelakang koma
print(format_str)
angka = 2004.54321
format_str = f"ribuan = {angka:010.3f}" #menampilkan landing zero(10 angka di depan)
print(format_str)

#format angka minus
angka_minus = -8
angka_plus = 8
format_minus = f"angka minus : {angka_minus:+d}"
format_plus = f"angka plus : {angka_plus:+d}"
print(format_minus)
print(format_plus)

#format persen (%)
persen = 10
format_persen = f"persen = {persen:.2%}"
print(format_persen)

#operasi aritmatika
harga = 20000
jumlah = 5
format_string = f"total harga : Rp.{harga * jumlah:,}"
print(format_string)

#format angka lain
angka = 10
binary = f"binary : {bin(angka)}"
octal = f"oktal : {oct(angka)}"
hex = f"hex : {hex(angka)}"
print(angka)
print(binary)
print(octal)
print(hex)
print("""
angka
binary
oktal
hexa
""")#pengganti \n alias Enter