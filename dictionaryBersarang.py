import datetime

mahasiswa1 = {
    "nama":"supri",
    "nim":'1',
    "sks": 20,
    "beasiswa":True,
    "lahir":datetime.datetime(2000,10,20)
}
mahasiswa2 = {
    "nama":"dadang",
    "nim":'2',
    "sks": 20,
    "beasiswa":False,
    "lahir":datetime.datetime(2001,10,20)
}
mahasiswa3 = {
    "nama":"nanang",
    "nim":'3',
    "sks": 20,
    "beasiswa":True,
    "lahir":datetime.datetime(2002,10,20)
}

data_mahasiswa = {
    'M001':mahasiswa1,
    'M002':mahasiswa2,
    'M003':mahasiswa3
}

print(f"{'key':<6} {'nama':<17} {'sks':<3} {'beasiswa':<9} {'lahir':<10}")
print('='*50)

for key in data_mahasiswa:
    KEY = key
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEA:<9} {LAHIR:<10}")