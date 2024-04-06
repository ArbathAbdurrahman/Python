# Fungsi rekursif dengan pendekatan linear
def hitung_faktorial_linear(n):
    if n == 0:
        return 1
    else:
        return n * hitung_faktorial_linear(n - 1)

# Fungsi rekursif dengan pendekatan direct
def hitung_faktorial_direct(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return hitung_faktorial_direct(n - 1, n * accumulator)

# Fungsi rekursif dengan pendekatan tail
def hitung_faktorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return hitung_faktorial_tail(n - 1, n * accumulator)

# Meminta masukan pengguna
n = int(input("Masukkan nilai integer untuk dihitung faktorial: "))

# Menghitung faktorial dengan pendekatan linear
hasil_hitung_faktorial_linear = hitung_faktorial_linear(n)
print(f"{n}! = {hasil_hitung_faktorial_linear} (Linear)")

# Menghitung faktorial dengan pendekatan direct
hasil_hitung_faktorial_direct = hitung_faktorial_direct(n)
print(f"{n}! = {hasil_hitung_faktorial_direct} (Direct)")

# Menghitung faktorial dengan pendekatan tail
hasil_hitung_faktorial_tail = hitung_faktorial_tail(n)
print(f"{n}! = {hasil_hitung_faktorial_tail} (Tail)")

# Fungsi rekursif dengan pendekatan linear
def hitung_faktorial(n:int)->int:
    if n == 0:
        return int(1)
    else :
        return int(n * hitung_faktorial(n - 1))

# Fungsi rekursif dengan pendekatan direct
def hitung_faktorial_direct(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return hitung_faktorial_direct(n - 1, n * accumulator)

# Fungsi rekursif dengan pendekatan tail
def hitung_faktorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return hitung_faktorial_tail(n - 1, n * accumulator)

# Meminta masukan pengguna
n:int = int(input("Masukkan nilai integer untuk dihitung faktorial: "))

# Menghitung faktorial dengan pendekatan linear
hasil_hitung_faktorial:int = hitung_faktorial(n)
print(f"{n}! = {hasil_hitung_faktorial}.")

# Menghitung faktorial dengan pendekatan direct
hasil_hitung_faktorial_direct = hitung_faktorial_direct(n)
print(f"{n}! = {hasil_hitung_faktorial_direct} (Direct)")

# Menghitung faktorial dengan pendekatan tail
hasil_hitung_faktorial_tail = hitung_faktorial_tail(n)
print(f"{n}! = {hasil_hitung_faktorial_tail} (Tail)")