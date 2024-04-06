import os

# panjangRuang:float=float(input("panjang ruang = "))
# lebarRuang:float=float(input("lebar ruang = "))
# tinggiRuang:float=float(input("tinggi ruang = "))
# def hitungCat(panjangRuang:float,lebarRuang:float,tinggiRuang:float)->float:
#     kelilingRuang=2*(panjangRuang+lebarRuang)
#     jumlahLiter = kelilingRuang * tinggiRuang / 12
#     return jumlahLiter

# jumlahLiter:float= hitungCat(panjangRuang,lebarRuang,tinggiRuang)
# print(f"Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter.")

# landArea:float=float(input("Area : "))
# landwidth:float=float(input("Width : "))
# landlength:float=float(input("Length : "))

# def checkArea(landArea,width,length)->bool:
#     buildingArea = width * length
#     if buildingArea <= landArea:
#         checkArea = True
#     else:
#         checkArea = False
#     return checkArea
# check:bool = checkArea(landArea,landwidth,landlength)
# if check == False:
#     print("Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut.")
# elif check ==True:
#     print("Rumah dapat dibangun berdasarkan ketiga nilai tersebut.")
# else :
#     print("Gagal")

os.system("cls")
permission:int=int(input("Permission : "))
city:str=str(input("city : "))

if permission == 1 :
    permission = True
elif permission == 0 :
    permission = False

def checkpermission(permission,city)->str:
    if permission ==False:
        print(f"Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap.")
    elif permission == True :
        print(f"Anda dapat membangun rumah di kota {city}.")
    return checkpermission

checkpermission(permission,city)
