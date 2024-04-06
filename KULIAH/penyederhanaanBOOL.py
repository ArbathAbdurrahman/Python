def Pbool(x,y,z):
    return x or y or z

print("HASIL PERHITUNGAN 1 FUNSI 3 VARIABEL")
pertama = Pbool(False,False,False)
print(pertama)
kedua = Pbool(False,True,False)
print(kedua)
ketiga = Pbool(False,True,True)
print(ketiga)
keempat = Pbool(True,True,True)
print(keempat)
Total = print("TOTAL = ",pertama or kedua or ketiga or keempat)



print("\n")

def vorvar(a,b,c,d):
    return a or b or c or d

print("HASIL PERHITUNGAN 1 FUNSI 4 VARIABEL")
satu = vorvar(False,False,False,True)
print(satu)
dua = vorvar(False,False,True,True)
print(dua)
tiga = vorvar(True,False,False,True)
print(tiga)
empat = vorvar(True,False,True,True)
print(empat)
lima = vorvar(True,True,True,True)
print(lima)
enam = vorvar(False,True,True,True)
print(enam)
total = print("TOTAL = ",satu or dua or tiga or empat or lima or enam)

print("\n")










# def fungsi(a,b,c,d):
#     hasil = (a and b) and (c and d)
#     final = hasil and (a and c)
#     return final

# pertamax = fungsi(x,y,x,y)
# print(f"{x,y,x,y} = {pertamax}")
# print(type(pertamax))
