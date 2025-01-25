# Manipulasi List(Operasi List)
print("\n" + "=" * 10 + "Manipulasi List" + "=" * 10 + "\n")

# Index  0(-3)   1(-2)   2(-1)
data = ["Ucup","Otong","Dudung"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

data_terakhir = data[-1]  # Misal gk tahu jkumlah data nya berapa, maka bisa menggunakan -1
print(f"Data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"Data Ucup adalah = {data_ucup}")

# Mengambil info jumlah data dlm List
print("\n" + "=" * 4 + "Mengambil info jumlah data dlm List" + 4 * "=")
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")


## Manipulasi data List 
print("\n" + "=" * 4 + "Manipulasi data List" + 4 * "=")

# Menambahkan item pada List sesuai posisi
print(f"Data sebelum ditambah = {data}")
print("\n" + "=" * 2 + "Menambahkan item pada List sesuai posisi" + 2 * "=")
# data.insert(posisi,item)
data.insert(1,"Asep")
print(f"Data sesudah ditambah = {data}")

# Menambah di akhir List
print("\n" + "=" * 2 + "Menambah di akhir List" + 2 * "=")
data.append("Jajang")
print(f"Data ditambah lagi = {data}")

# Menambahkan List dg List
print("\n" + "=" * 2 + "Menambahkan List dg List" + 2 * "=")
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"Data gabungan = {data}")

# Merubah Data
print("\n" + "=" * 2 + "Merubah Data" + 2 * "=")
# Kita ubah data 2 menjadi Michael
data[2] = "Michael"
print(f"Data rubah = {data}")

# Menghapus/Remove Data 
print("\n" + "=" * 2 + "Menghapus/Remove Data" + 2 * "=")
data.remove("Ujang")
print(f"Data remove = {data}")
# data.remove("usep") akan error krn gk ada di List


# Menghapus/Remove Data paling belakang
print("\n" + "=" * 2 + "Menghapus/Remove Data paling belakang" + 2 * "=")
data_akhir = data.pop()
print(f"Data Akhir = {data}")
print(data_akhir)






































































































print("\n")