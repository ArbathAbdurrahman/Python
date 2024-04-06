import time
import random
import os

os.system("cls")
start = input("Ketik 1 untuk Hack NASA :")
def njdsfj():
    progress = 0
    while progress <= 100:
        time.sleep(0.1)
        random_incrment = random.randint(1, 2)
        progress += random_incrment
        progress = min(progress, 100)
        print(f"\rHacking Nasa {progress}%", end='', flush=True)
        if progress < 100:
            print("\n", end= '', flush=True)
        if progress >= 100:
            print("\nNasa Hack Successfully")
            break
njdsfj()