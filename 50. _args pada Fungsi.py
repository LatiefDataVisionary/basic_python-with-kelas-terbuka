### *args pada Fungsi
print("\n" + "=" * 10 + "*args pada Fungsi" + "=" * 10 + "\n")


## Memasukkan Data/Argument
print("===Memasukkan Data/Argument")

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Otong",100,120])


## Kenanalan dg *args
print("\n===Kenanalan dg *args")

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Dudung",120,120)


## Studi Kasus

def tambah(*data):
    # Data tipenya adalah tuple, dia bisa di iterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"Hasil = {hasil}")














































































































print("\n")