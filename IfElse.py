import time
import random

nama = input(f"tulis nama anda \t: ")
# if kondisi : aksi | else : jika if salah maka
if nama=="Udin" : 
    progress = 0
    while progress <= 100:
        time.sleep(0.1)
        random_incrment = random.randint(1, 10)
        progress += random_incrment
        progress = min(progress, 100)
        print(f"\rMengecek User {progress}%", end='', flush=True)
        if progress < 100:
            print("\n", end= '', flush=True)
        if progress >= 100:
            sandi = input(f"\nVerifikasi sandi \t: ")
            break
    if sandi == "octagram" :
            progress = 0
    while progress <= 100:
        time.sleep(0.1)
        random_incrment = random.randint(1, 10)
        progress += random_incrment
        progress = min(progress, 100)
        print(f"\rVerifikasi Sandi {progress}%", end='', flush=True)
        if progress < 100:
            print("\n", end= '', flush=True)
        if progress >= 100:
            print("\n")
            print("="*25)
            print(f"Selamat Datang Lord {nama}")
            print("="*25)
            break
    else :
        print(f"Verifikasi gagal")
elif nama == "Priscilla" :
    progress = 0
    while progress <= 100:
        time.sleep(0.1)
        random_incrment = random.randint(1, 10)
        progress += random_incrment
        progress = min(progress, 100)
        print(f"\rMengecek User {progress}%", end='', flush=True)
        if progress < 100:
            print("\n", end= '', flush=True)
        if progress >= 100:
            print("\n")
            print("="*30)
            print(f"Selamat Datang Ratu {nama}")
            print("="*30)
            break
else:
    print("invalid")