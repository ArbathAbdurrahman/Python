import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    while(True):
        match sistem_operasi:
            case 'posix': os.system('clear')#kalau memakai os linux & mac
            case 'nt': os.system('cls')#kalau memakai os windows

        print("SELAMAT DATANG")
        print("DATABASE PERPUSTAKAAN")
        print("="*20)

        print(f'1. Create')
        print(f'2. Read')
        print(f'3. Update')
        print(f'4. Delete')
        user_opsi = input("masukan opsi : ")

        print("\n====================\n")

        match user_opsi:
            case "1":print("Create Data")
            case "2":print("Read Data")
            case "3":print("Update Data")
            case "4":print("Delete Data")

        print("\n====================\n")
        isdone = input("apakah selesai? (y) : ")
        if isdone == "y" or "Y":
            break