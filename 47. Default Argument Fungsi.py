### DEFAULT ARGUMENT FUNGSI
print("\n" + "=" * 10 + "DEFAULT ARGUMENT FUNGSI" + "=" * 10 + "\n")

# def fungsi(argument)
# def fungsi(argument = nilai defaultnya)

## Contoh 1
print("===Contoh 1")
def say_hello(nama = "Ganteng"):
    '''Fungsi dg Default Argument'''
    print(f"Hello {nama}!")

say_hello("Ucup")
say_hello()

def sapa_dia(pesan,nama):
    '''Fungsi dg satu input biasa, dan satu default argument'''
    print(f"Hai {nama}, {pesan}!")

sapa_dia("Hai Ganteeeeeng","Dudung")

## Contoh 2
print("\n===Contoh 2")
def sapa_dia(nama, pesan = "Apa kabar"):
    '''Fungsi dg satu input biasa, dan satu default argument'''
    print(f"Hai {nama}, {pesan}!")

sapa_dia("Dudung","Hai Ganteeeeeng")
sapa_dia("Otong")


## Contoh 3
print("\n===Contoh 3")
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat = 2, angka = 5)
print(hasil)


def hitung_pangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat = 3, angka = 5)
print(hasil)


## Contoh 4
print("\n===Contoh 4")
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
    hasil = input1 + input2 + input3 + input4 
    return hasil

print(fungsi())
print(fungsi(input3 = 10))


































































































print("\n")
