data = {
    "mm":"mamank",
    "sp":"supri",
    "nn":"nanang",
    "dd":"dadang"
}

fren = data.copy()

print(f"\nsebelum di copy : {data}\n")
print(f"fren copy : {fren}\n")

data["dd"]="dadang gantenk"
print(f"\ndata tidak ikut berubah : {data}\n")
print(f"fren copy : {fren}\n")

# pop dictionary
datafren = fren.pop("dd")
print(f"\ndata yang diambil : {datafren}\n")
print(f"dadang hilang : {fren}\n")

#pop item dictionary
dataakhir = fren.popitem()
print(f"data terakhir : {dataakhir}")
print(f"dadang hilang : {fren}\n")