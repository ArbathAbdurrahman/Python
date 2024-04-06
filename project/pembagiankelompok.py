import random
import os

os.system('cls')
# anggota kelas informatika A
print("Audi Bayu Sirly Ghina Puput Khanan Vina Arham AnnisaIF Anggraini Agung Arbath Salman Azza Rafli Alan Zamroni Nasywa Zahra Inara Ara Nadine AkmalMaeng Chairul Hanif Azzam Nabil AkmalGoldi AlGhazali Fahalliza Faris Ariya DzakyDanarta Akbar Radipta AkmalSani Vikri MaulanaZakki Emul Yusran Adam Abit Shobaru Aslam Naufal DwiE Fauzan Kaka DzakyErlanda Faiz")
# Meminta pengguna untuk memasukkan anggota list, dipisahkan oleh spasi
user_input = input("Masukkan semua anggota kelompok dipisahkan oleh spasi dan pastikan anggota dapat dibagi seecara merata! \n--> ")

# Meminta pengguna memasukkan jumlah kelompok yang akan dibuat
kelompok_input = int(input("Masukkan jumlah kelompok yang akan dibuat! \n-->"))

# Mengonversi string input menjadi list
members = [str(item) for item in user_input.split()]

# Mengacak urutan anggota
random.shuffle(members)

# Membagi anggota menjadi n kelompok
kelompok = kelompok_input
anggota = len(members) // kelompok

grup = [members[i:i + anggota] for i in range(0, len(members), anggota)]

# Cetak hasil
print("Hasil Pembagian Kelompok :")
for i, group in enumerate(grup, 1):
    print(f"Kelompok {i} : {group}")
