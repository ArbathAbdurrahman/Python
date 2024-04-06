import time
import random
userinput = input("Masukan Sandi :")
def njdsfj():
    progress = 0
    while progress <= 100:
        time.sleep(0.1)
        random_incrment = random.randint(1, 10)
        progress += random_incrment
        progress = min(progress, 100)
        print(f"\rMenebak Sandi {progress}%", end='', flush=True)
        if progress < 100:
            print("\n", end= '', flush=True)
        if progress >= 100:
            print("\nMenebak Sandi Sukses")
            break
njdsfj()
print("ingin melihat hasil?")
hasil = input("ketik 1 untuk menampilkan hasil : ")
if hasil == 1:
    print(f"Sandi Anda : {userinput}")
else:
    print("sandi tidak ditampilkan")

