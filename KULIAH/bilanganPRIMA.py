def prima(n):# sebuah fungsi untuk mengecek bilangan prima
    # apakah bilangan lebih dari 1?
    if n <= 1:
        # jika tidak maka
        return False
    # mengeck apakah ada faktor lain selain 1 dan n yg dpt membagi n (mengeck bilangan prima)
    for i in range(2, int(n**0.5)+1): 
        #apakah i adalah faktor dari n?
        if n % i == 0:
            #jika ya maka
            return False
    # jika ada faktor lain selain 1 dan n yg dpt membagi n maka
    return True
    
while True :# kondisi dimana program akan terus berjalan
    #meminta input bilangan
    cek_bilangan = int(input("masukan bilangan : "))
    # mengecek apakah bilangan menghasilkan True
    if prima(cek_bilangan):
        # jika True maka tampilkan
        print(f"{cek_bilangan} adalah bilangan prima")
    # jika False maka
    else:
        # tampilkan
        print(f"{cek_bilangan} bukan bilangan prima")