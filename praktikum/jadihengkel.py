import time
import random
import os

# data = 'prinf("hello world")'
os.system("cls")
user = input()
hh = "="*28
def njdsfj():
    progress = 0
    while progress <= 100:
        time.sleep(0.1)
        random_incrment = random.randint(10, 20)
        progress += random_incrment
        progress = min(progress, 100)
        print(f"\r{progress}%", end='', flush=True)
        if progress < 100:
            print("\n", end= '', flush=True)
        if progress >= 100:
            print(f"\n{hh}\nSelamat Anda Menjadi Hengkel\n{hh}")
            break
njdsfj()

# if user == data:
#     print("Selamat anda menjadi Hengkel")

# else:
#     print("anda gagal menjadi Hengkel")
