# continue, pass, break
# pass = ada tp tidak akan dieksekusi
# break = kebalikan continue loncat ke akhir loop

angka = 0
while angka < 10:
    angka += 1
    print(f"angka sekarang = {angka}" )

    if angka == 7 :
        print("nice")
        continue #langsung loncat ke awal loop

    print("lanjut") #terSkip

print("udah bang")