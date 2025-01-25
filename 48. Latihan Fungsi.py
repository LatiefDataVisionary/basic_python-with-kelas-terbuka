### LATIHAN FUNGSI
print("\n" + "=" * 10 + "LATIHAN FUNGSI" + "=" * 10 + "\n")

import os 

# Program menghitung luas dan keliling persegi panjang

# # Membuat header program
# while True:
# os.system("cls")
# print(f"{'PROGRAM MENGITUNG LUAS':^40}")
# print(f"{'DAN KELILING PESRSEGI PANJANG':^40}")
# print(f"{'_' * 40: ^40}")

# # Mengambil Input User
# LEBAR = int(input("Masukkan nilai lebar: "))
# PANJANG = int(input("Masukkan nilai panjang: "))

# # Program Menghitung Luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG + LEBAR)

# # Tampilkan Hasilnya
# print(f"Hasil perhitungan Luas = {LUAS}")
# print(f"Hasil perhitungan Keliling = {KELILING}")

def header():
    '''Fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'_' * 40: ^40}")

def bawah_header():
    print("Silahkan Pilih!")
    print("1. Menhitung Luas")
    print("2. Menhitung Keliling")
    print("3. Menhitung Luas & Keliling")

def input_user():
    '''Fungsi Input User'''
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''
    return lebar * panjang
    
def hitung_keliling(lebar,panjang):
    '''Fungsi Keliling'''
    return 2 * (lebar * panjang)

def display(message,value):
    '''Fungsi Display'''
    print(f"Hasil perhitungan {message} = {value}")

# Program utamanya
while True:
    header()
    bawah_header()
    opsi = int(input("Masukkan pilihan Anda: "))

    if opsi not in [1, 2, 3]:
        print("Masukkan pilihan nomor yang tersedia!")
        continue

    LEBAR, PANJANG = input_user()

    if opsi == 1:
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("Luas", LUAS)

    elif opsi == 2:
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("Keliling", KELILING)

    elif opsi == 3:
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)

        display("Luas", LUAS)
        display("Keliling", KELILING)

    isContinue = input("Apakah lanjut (y/n)?: ")
    if isContinue == "n":
        break

print("Program Selesai, terima kasih!!")


































































































print("\n")