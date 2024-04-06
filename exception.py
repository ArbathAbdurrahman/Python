while(True):
    try: #bila program try eror 
        angka = int(input("Massukan angka : "))
        hasil = 10/angka
        print(f"hasil : {hasil}")
        done = input("selesai? (y/n)")
        if done == "y":
            break

    except: #maka akan menjalankan program except
        print("format salah")
print("akhir program")