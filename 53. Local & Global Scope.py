### Global & Local Scope
print("\n" + "=" * 10 + "Global & Local Scope" + "=" * 10 + "\n")

nama_global = "Otong"  # Variabel Global

# Akses Variabel Global dlm Fungsi
print("\n===Akses Variabel Global dlm Fungsi")
def fungsi1():
    print(f"Fungsi menampilkan {nama_global}")

fungsi1()


# Akses Variabel Global dlm Loop
print("\n===Akses Variabel Global dlm Loop")
for i in range(0,5):
    print(f"Loop {i} - {nama_global}")


# Percabangan 
print("\n===Akses Variabel Global dlm Percabangan")
if True:
    print(f"If menampilkan {nama_global}")



## Variabel Lokal Scope
print("\n====Variabel Lokal Scope====")

def fungsi2():
    nama_local = "Ucup" # Variabel Lokal Scope

fungsi2()
# print(nama_lokal)  # tdk bisa dilakukan boss


## Contoh 1: Penggunaan Akses Variabel
print("\n====Contoh 1: Penggunaan Akses Variabel")
def say_otong():
    print(f"Hello {nama}!")

nama = "Otong"
say_otong()

## Contoh 2: Merubah Variabel Global
print("\n====Contoh 2: Merubah Variabel Global")

angka = 0
name = "Ucup"

def ubah(nilai_baru,nama_baru):
    global angka  # Fungsi ini mendpt akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru


print(f"Sebelum = {angka,name}")
ubah(10,"Otong")
print(f"Sesudah = {angka, name}")


## Contoh 3:
print("\n====Contoh 3:")

angka = 0 

for i in range(0,5):
    angka += 1
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)


























































































































print("\n")