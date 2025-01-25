# Operasi List 
print("\n" + "=" * 10 + "Operasi List" + "=" * 10 + "\n")

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"Data Angka = {data_angka}")

# Count Data 
# Utk mendeteksi Statistik
# Menghitung Data angkanya muncul berapa kali 
print("\n" + "=" * 3 + "Count Data" + "=" * 3)

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"Jumlah angka 4 = {jumlah_data_4}")
print(f"Jumlah angka 3 = {jumlah_data_3}")

# Ambil Posisi Data (Index)
print("\n" + "=" * 3 + "Ambil Posisi Data (Index)" + "=" * 3)
data = ["Ucup","Otong","Dudung","Ujang"]
print(f"Data = {data}")

index_dudung = data.index("Dudung")
print(f"Index si Dudung = {index_dudung}")

index_ujang = data.index("Ujang")
print(f"Index si Ujang = {index_ujang}")

# data.index("Usep")


# Mengurutkan List (Dari angka terkecil ke terbesar)
print("\n" + "=" * 3 + "Mengurutkan List" + "=" * 3)
print(f"Data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"Data angka sort = {data_angka}")

print(f"Data = {data}")  # Diurutkan berdasarkan abjad
data.sort()
print(f"Data sort = {data}")


# Balik List
print("\n" + "=" * 3 + "Balik List" + "=" * 3)
# Syaratnya harus di urutkan terlebih dahulu (kalo ga salah wkwkwkwk)
data_angka.reverse()
data.reverse()
print(f"Data direverse = {data_angka}")
print(f"Data direverse = {data}")





























































































































print("\n")