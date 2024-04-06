import random

# Membuat list dengan 50 anggota (misalnya, nomor 1 hingga 50)
members = list(range(1, 51))

# Mengacak urutan anggota
random.shuffle(members)

# Membagi anggota menjadi 7 kelompok
num_groups = 11
group_size = len(members) // num_groups

groups = [members[i:i + group_size] for i in range(0, len(members), group_size)]

# Cetak hasil
for i, group in enumerate(groups, 1):
    print(f"Kelompok {i}: {group}")
