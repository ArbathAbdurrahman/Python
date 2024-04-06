import datetime as dt 

hari_ini = dt.date.today()
print(f"hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2000,2,20)
print("tanggal",tanggal, f"adalah hari {tanggal:%A}")

print("silahkan masukan hari lahir anda :")
tanggal = int(input("tanggal :")) #int untuk merubah string mjd integer agar bisa dibaca program
bulan = int(input("bulan \t:"))
tahun = int(input("tahun \t:"))
tanggal_user = dt.date(tahun,bulan,tanggal)
umur = hari_ini - tanggal_user
tahun_user = umur // 365
hari_user = (umur.days % 365) // 30
hari_umur = hari_user // 1
print("tanggal",tanggal_user, f"adalah hari {tanggal_user:%A}")
print(f"umur anda : \n{umur.days} hari")
print(f"{tahun_user.days} tahun {hari_user} bulan {hari_umur} hari")