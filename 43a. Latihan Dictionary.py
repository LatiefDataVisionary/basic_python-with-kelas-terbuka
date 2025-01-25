## LATIHAN DICTIONARY
print("\n" + "=" * 10 + "LATIHAN DICTIONARY" + "=" * 10 + "\n")

import datetime
import os

# Template Dict Mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system("cls")  # Utk Windows
# os.system("clear")  # Utk Linux, Mac, Unique
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASIWA':^20}")
print("_" * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] =int(input("SKS Mahasiswa: "))
TAHUN_LAHIR = int(input("Tahun lahir (yyyy): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)











































































































print("\n")