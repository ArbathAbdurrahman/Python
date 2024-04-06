data = {
    "mm":"mamank",
    "sp":"supri",
    "nn":"nanang",
    "dd":"dadang"
}

#yang keluar hanya key
for oye in data:
    print(oye)
#operator untuk mengambil item
keys = data.keys()
print(keys)
for key in data.keys():
    print(data.get(key))
#mengambil value
for value in data.values():
    print(value)
#mengambil item
items = data.items()
print(items)#semua item
for item in data.items():
    print(item)#inti item

for key,value in data.items():
    print(f"key = {key} value = {value}")