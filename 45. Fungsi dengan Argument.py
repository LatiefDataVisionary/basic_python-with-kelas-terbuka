## FUNGSI DENGAN ARGUMENT
print("\n" + "=" * 10 + "FUNGSI DENGAN ARGUMENT" + '=' * 10 + "\n")

'''Fungsi dg Argument (Input)'''

'''
def nama_fungsi(argument/parameter/input):
    # badan fungsi
'''

def hello_world(nama):
    '''Fungsi hellow world menerima input dg variabel nama'''
    print(f"Selamat datang dunia wahai {nama}!")

hello_world("Ucup")
hello_world("Latief si Ganteng")
hello_world(99)
hello_world(True)

# Program Tambah
print("\n=== Program Tambah")
def tambah(angka_1,angka_2):
    '''Fungsi Tambah'''
    hasil = angka_1 + angka_2
    print(f"Hasil dari {angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(True,True)
tambah(False,True)
tambah(False,False)

print("\n")
def say_hi(list_peserta):
    '''Fungsi say hi'''
    list_peserta[1] = "Asyep"
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup","Otong","Dudung"]

say_hi(anggota_boyband)
print(anggota_boyband[1])































































































































print("\n")