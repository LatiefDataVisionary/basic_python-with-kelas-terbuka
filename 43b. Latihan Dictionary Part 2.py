## LATIHAN DICTIONARY PART 2
print("\n" + "=" * 10 + "LATIHAN DICTIONARY PART 2" + "=" * 10 + "\n")

import datetime
import os
import string
import random

# Template Dict Mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")  # Utk Windows
    # os.system("clear")  # Utk Linux, Mac, Unique
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASIWA':^20}")
    print("_" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] =int(input("SKS Mahasiswa: "))
    TAHUN_LAHIR = int(input("Tahun lahir (yyyy): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))  # Maximum ada 6 random numbers
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS':<3} {'Lahir':<10}")
    print("-" * 50)
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {'NIM':<8} {SKS:<3} {LAHIR:<10}")

    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)?: ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih!")























































































































print("\n")