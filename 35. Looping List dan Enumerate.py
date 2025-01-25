# Looping List dan Enumerate 
print("\n" + "=" * 10 + "Looping List dan Enumerate" + "=" * 10 + "\n")

# Looping dari List 
print("Looping dari List")
# For Loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"Angka = {angka}")

tanggal_lahir = [18,10,2004]
for angka_lahir in tanggal_lahir:
    print(f"Angka Lahir = {angka_lahir}")

peserta = [ "Ucup","Otong","Dadang","Diding","Dudung"]
for nama in peserta:
    print(f"Nama = {nama}")

# For Loop dan Range
print("\nFor Loop dan Range")

kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka = {kumpulan_angka[i]}")


# While Loop
print("\nWhile Loop")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"Angka = {kumpulan_angka[i]}")
    i += 1


# List Comprehension (agar lebih singkat)
print("\nList Comprehension")
kumpulan_angka = [10,5,4,2,6,5]
data = ["Ucup",1,2,3,"Otong"]

[print(f"Data = {i}") for i in data]

angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# Enumerate 
print("\n" + "=" * 4 + "Enumerate" + "=" * 4)
# enumerate itu akan mengambil index dan datanya 
# dg menggunakan enumerate bisa menghilangkan for loop dan range
data_list = ["Ucup",1,2,3,"Otong"]

for index,data in enumerate(data_list):
    print(f"Index = {index}, Data = {data}")









































































































































print("\n")