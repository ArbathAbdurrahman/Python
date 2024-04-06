#menghitung biaya pondok
modal = int(input("masukan uang saat ini : Rp."))
daftar = int(input("masukan biaya pendaftaran : Rp."))
spp = int(input("masukan spp perbulan : Rp."))
makan = int(input("masukan biaya makan perhari : Rp."))
bensin = int(input("masukan biaya bensin perminggu : Rp."))
kuota = int(input("masukan biaya kuota perbulan : Rp."))
lain = int(input("masukan biaya lain-lain perbulan : Rp."))
tahun = daftar+((spp+(makan*30)+(bensin*4)+kuota+lain)*12)
bulan = (daftar/12)+((spp+(makan*30)+(bensin*4)+kuota+lain))
print(f"uang saat ini : Rp.{modal:,}")
print(f"total biaya pondok : Rp.{tahun:,}")
print(f"biaya pondok perbulan : Rp.{bulan:,}")
if modal > tahun:
    print(f"uang anda sisa Rp.{modal - tahun :,}")
elif modal < tahun :
    print(f"uang anda kurang Rp.{tahun - modal :,}")
else:
    print("uang anda mencukupi")