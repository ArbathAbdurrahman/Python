data = {
    "mm":"mamank",
    "sp":"supri",
    "nn":"nanang"
}
#panjang dictionary
panjang = len(data)
print(f"panajang data = {panjang}")

#mengecek key exist atau tidak
key = "nn"
cekkey = key in data
print(f"apakah {key} ada pada data = {cekkey}")

#mengakses value (read) dengan get
print(data["sp"])
print(data.get("mm"))
print(data.get("kk"))#cek key dengan get

#UPDATE
data["sp"] = "supri ganteng"
print(data)
data.update({"dd":"dadang"})#akan menambahkann jika key tidak ada pada data
print(data)

#DELETE
del data["dd"]
print(data)#menghapus key dd
