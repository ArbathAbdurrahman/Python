# membuat segi tiga

sisi = 10
count = 1 #dummy variable

for i in range(sisi):
    print("*"*count)
    count += 1
print("end of program\n")

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi :
        break
print("end of program\n")

count = 1
while True:
    if (count%2):#menggunakan modulus
        print("*"*count) #print jika ganjil
        count += 1
    else: #kembali keatas jika ganjil
        count += 1
        continue
    if count > sisi : #berhenti jika melebihi sisi
        break
print("end of program\n")


count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"*"*count) #print jika ganjil
        spasi -= 1
        count += 1
    else: #kembali keatas jika ganjil
        count += 1
        continue
    if count > sisi : #berhenti jika melebihi sisi
        break
count = sisi
spasi = 1
while True:
    if (count%2):
        print(" "*spasi,"*"*count) #print jika ganjil
        spasi += 1
        count -= 1
    else: #kembali keatas jika ganjil
        count -= 1
        continue
    if count <= 0 : #berhenti jika melebihi sisi
        break
