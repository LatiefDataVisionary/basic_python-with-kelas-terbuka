# # Operasi dan Manipulasi String

# # 1. Menyambung String (Concantenate)
# nama_pertama = "Ucup"
# nama_tengah = "D"
# nama_akhir = "Fame"

# nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
# print(nama_lengkap)

# # 2. Menghitung panjang string
# panjang = len(nama_lengkap)
# print("Panjang dari " + nama_lengkap + " = " + str(panjang))

# # 3. Operator untuk String

# # Mengecek apakah ada komponen Char atau String di String

# d = "\nD"
# status = d in nama_lengkap
# print(d + " ada di " + nama_lengkap + " = " + str(status))

# d = "Ucup"
# status = d in nama_lengkap
# print(d + " ada di " + nama_lengkap + " = " + str(status))

# d = "d"
# status = d in nama_lengkap
# print(d + " ada di " + nama_lengkap + " = " + str(status))

# d = "d"
# status = d not in nama_lengkap
# print(d + " tidak ada di " + nama_lengkap + " = " + str(status))
# print("\n")

# # Mengulang String 
# print("Wk" * 10)
# print(15 * "Wk")

# # Indexing = Mengambil data dari String / Motong motong
# print("Index ke-0 : " + nama_lengkap[0])
# print("Index ke-1 : " + nama_lengkap[1])
# print("Index ke-6 : " + nama_lengkap[6])
# print("Index ke-(-1) : " + nama_lengkap[-1])  # Mengambil dari belakang
# print("Index ke-(-2) : " + nama_lengkap[-2])  # Mengambil dari belakang
# print("Index ke-[0,3] : " + nama_lengkap[0:3])
# print("Index ke-[0,3] : " + nama_lengkap[0:4])
# print("Index ke-[3,7] : " + nama_lengkap[3:8])
# print("Index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2])
# print("Index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])


# # Item paling kecil 
# print("Paling kecil : " + min(nama_lengkap)) # Adalah spasi

# # Item paling besar 
# print("Paling besar : " + max(nama_lengkap)) # Muncul u karena u paling akhir di abjad

# ascii_code = ord(" ")
# print("ASCII code untuk spasi adalah " + str(ascii_code)) 
# data = 117
# print("Char untuk ASCII 117 adalah " + chr(data)) 
# ascii_code = ord("'")
# print("ASCII code untuk spasi adalah " + str(ascii_code)) 

# # 4. Operator dlm bentuk Method 
# data = "otong surotong pararotong"
# jumlah = data.count("o")
# print("Jumlah o pada " + data + " = " + str(jumlah))
# jumlah = data.count("g")
# print("Jumlah g pada " + data + " = " + str(jumlah))

print("hhh")
print("\n"*4)
nama = str(input("Masukkan nama: "))#.upper()
huruf1 = str(input("Masukkan huruf yang dicari: "))#upper()
#huruf = huruf1.upper()
jumlah = nama.count(huruf1)
print(f"Jumkah huruf {huruf1} pada nama {nama} adalah {jumlah}")



















































































