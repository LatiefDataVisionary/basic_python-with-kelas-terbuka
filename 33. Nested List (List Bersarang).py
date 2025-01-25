# Nested List/List Bersarang
print("\n" + "=" * 10 + "Nested List/List Bersarang" + "=" * 10 + "\n")

data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print(f"List biasa = {data_list_biasa}")

list_2D = [data_0,data_1]
print(f"List 2D = {list_2D}")

list_2D = [data_0,data_1,data_list_biasa]
print(f"List 2D = {list_2D}")

list_2D = [data_0,data_1,6,7]  # Campuran antara List dan Angka
print(f"List 2D = {list_2D}")

# Nested List digunakan untuk Data Berseri

# Contoh Penggunaan
print("\n" + "=" * 3 + "Contoh Pengunaan" + "=" * 3)
peserta_0 = ["Ucup",25,"Laki-laki"]
peserta_1 = ["Otong",10,"Laki-laki"]
peserta_2 = ["Dedeh",50,"Wanita"]
list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"Peserta = {list_peserta}\n")

for peserta in list_peserta:
    print(f"Nama\t = {peserta[0]}")
    print(f"Umur\t = {peserta[1]}")
    print(f"Gender\t = {peserta[2]}\n")



# Dengan Reference
print("\n" + "=" * 3 + "Dengan Reference" + "=" * 3)

list_copy = list_peserta.copy()
print(f"Peserta = {list_copy}\n")
peserta_0[0] = "Michael"
print(f"Peserta = {list_copy}\n")
print(f"Peserta = {list_peserta}\n")
















































































































print("\n")