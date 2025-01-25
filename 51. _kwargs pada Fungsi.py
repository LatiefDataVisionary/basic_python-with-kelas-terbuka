###  *kwargs pada Fungsi
print("\n" + "=" * 10 + "*kwargs pada Fungsi" + "=" * 10 + "\n")


def fungsi(nama,tinggi,berat):
    '''Fungsi Biasa'''
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg.")

fungsi("Ucup",183,79)


def fungsi(**kwargs):
    '''Fungsi Biasa'''
    print(kwargs)

fungsi(nama = "Ucup", tinggi = 183, berat= 79)


def fungsi(**kwargs):
    '''Fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg.")

fungsi(nama = "Ucup", tinggi = 183, berat= 79)


## Studi Kasus
print("\n===Studi Kasus")
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi!")

    return output


hasil = math(1,2,3,4,option = "tambah")

print(f"Hasil jumlah {hasil}")

hasil = math(1,2,3,4,option = "kali")
print(f"Hasil kali {hasil}")

































































































print("\n")