## ----LIST----
print("\n" + 10 * "-" + "LIST" + 10 * "-" + "\n")

angka = 1 
angka = 2
angka = 3

tuple = 1,

# Di Python tdk ada ARRAY kecuali di NUMPY
# Kumpulan Data Numbers 
print("=" * 4 + "Kumpulan Data Numbers" + 4 * "=" + "\n")
data_angka = [1,2,3]
print(data_angka)

# Kumpulan Data String 
print("=" * 4 + "Kumpulan Data String" + 4 * "=" + "\n")
data_string = ["Ucup","Otong","Odah"]
print(data_string)

# Kumpulan Data Boolean 
print("=" * 4 + "Kumpulan Data Boolean" + 4 * "=" + "\n")
data_boolean= [True, False, True, True]
print(data_boolean)

# Kumpulan Data Campuran 
print("\n" + "=" * 4 + "Kumpulan Data Campuran" + 4 * "=" + "\n")
data_campuran= [1,"bala-bala",2,"cireng","Ucup",True,"Otong",False]
print(data_campuran)

# Cara Alternatif Membuat List
print("\n" + "=" * 4 + "Cara Alternatif Membuat List" + 4 * "=")
data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

data_range = range(0,10,2)  # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat List dg For Loop, List Comprehension
print("\n" + "=" * 4 + "Membuat List dg For Loop, List Comprehension" + 4 * "=")
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)
# Hanya berlaku di Python

# Membuat List pake For pake IF
print("\n" + "=" * 4 + "Membuat List pake For pake IF" + 4 * "=")
list_pake_for_if = [i for i in range(0,10) if i != 5 ]
print(list_pake_for_if)
# merupakan cara membuat List yg lebih Advance

print("Yang Genap: ")
list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

print("Yang Ganjil: ")
list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)

print("Yang Ganjil di kuadratin: ")
list_pake_for_if = [i**2 for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)




# data_list = ['El', 'Nopal', 'Nabil', 'Ndaru']
# print(data_list)

# data_list[0] = 'Daniel'
# print(data_list)

# data_list.append('Erik')
# print(data_list)

# data_list.pop(-1)
# print(data_list)

# print(len(data_list))
# print((data_list))

# print(data_list[0:2])


# for i in data_list:
#     print(i)


# password = int(input(f"\nMasukkan password admin"))

# while True:
#     if password == 12345:
#         print("Selamat! Anda berhasil login sbg admin")
#     else:
#         print("Masukkan kodingan yang bener dong!!!")


























































































print("\n")
































































