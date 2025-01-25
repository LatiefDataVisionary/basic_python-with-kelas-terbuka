## FUNGSI DG RETURN/KEMBALIAN (RETURN VALUE)
print("\n" + "=" * 10 + "FUNGSI DG RETURN/KEMBALIAN" + "=" * 10 + "\n")

# template fungsi dg kembalian
# def nama_fungsi(argument):
#    badan fungsi
#    return output

# Fungsi Kuadrat 

def kuadrat(input_angka):
    '''Fungsi Kuadrat'''
    output_kuadrat = input_angka ** 2
    return output_kuadrat

x = kuadrat(3)
print(x)
print(f"Isi untuk X = {x}\n")

y = kuadrat(2)
print(y)
print(f"Isi untuk Y = {y}\n")

print(x * y)
print(f"Hasil {x} * {y} = {x * y}\n")

# z = kuadrat(int(input("Masukkan angka: ")))
# print(z)
# print(f"Hasil ({z} + {x}) * {y} = {(z + x) * y}\n")

zz = 10 + kuadrat(7)
print(zz)


## Fungsi Tambah
print("\n" + "=" * 3 + "Fungsi Tambah" + "=" * 3)

def fungsi_tambah(angka_1,angka_2):
    '''Fungsi Return dg multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(10,8)
print(a)


## Fungsi dg Return banyak
print("\n" + "=" * 3 + "Fungsi dg Return banyak" + "=" * 3)

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")





































































































print("\n")