# String Width and Multiline 

# Data
print("\nData")
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String Standard
print("\n" + 4 * "=" + "String Standard" + 4 * "=")
data_string = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Ukuran sepatu = {data_nomor_sepatu}"
print(5 * "=" + "Data String" + "=" * 5 )
print(data_string)

# String Multiline (Dengan menggunakan enter, newline, \n)
print("\n" + 4 * "=" + "String Multiline" + 4 * "=")
data_string = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nUkuran sepatu = {data_nomor_sepatu}."
print("\n" + 5 * "=" + "Data String" + "=" * 5 )
print(data_string)

# String Multiline (Kutip Tripleks)
print("\n" + 4 * "=" + "String Multiline (Kutip Tripleks)" + 4 * "=")
data_string = f"""Nama = {data_nama}  
Umur = {data_umur}
Tinggi = {data_tinggi}
Ukuran sepatu = {data_nomor_sepatu}
"""
print("\n" + 5 * "=" + "Data String" + "=" * 5 )
print(data_string)

# Mengatur Lebar
print("\n" + 4 * "=" + "Mengatur Lebar" + 4 * "=")
data_string = f"""Nama          = {data_nama}  
Umur          = {data_umur}
Tinggi        = {data_tinggi}
Ukuran sepatu = {data_nomor_sepatu}
"""
print("\n" + 5 * "=" + "Data String" + "=" * 5 )
print(data_string)

data_nama = "Ucup"  # Agar rata kanan 
data_string = f"""Nama          = {data_nama}  
Nama          = {data_nama:>5}  
Umur          = {data_umur:>5}
Tinggi        = {data_tinggi:>5}
Ukuran sepatu = {data_nomor_sepatu:>5}
"""
print("\n" + 5 * "=" + "Data String" + "=" * 5 )
print(data_string)

data_nama = "Ucup Surucup"  
data_tinggi = 105.17
data_string = f"""Nama          = {data_nama:>5}  
Umur          = {data_umur:>5}
Tinggi        = {data_tinggi:>5}
Ukuran sepatu = {data_nomor_sepatu:>5}
"""
print("\n" + 5 * "=" + "Data String" + "=" * 5 )
print(data_string)


































































































































print("\n")