# Operasi Manipulasi String Part 2
# Operator dlm bentuk Methods

## Merubah Case dari String

# Merubah semua ke Upper Case
print("\nMerubah semua ke Upper Case")
salam = "bro"
print("Normal = " + salam)
salam = salam.upper()
print("Upper = " + salam)


# Merubah semua ke Lower Case
print("\nMerubah semua ke Lower Case")
alay = "aKu KeCe AbieeezZzZZZZZ"
print("Normal = " + alay)
alay = alay.lower()
print("Upper = " + alay)

## Pengecekan dg IS X Method
# Contoh utk pengecekan Lower Case
print("\nContoh utk pengecekan Lower Case")
salam = "sist"
apakah_lower = salam.islower() # Hasilnya Bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # Hasilnya Bool
print(salam + " is upper = " + str(apakah_upper))
# So IS ini berguna utk mengecek dalamnya apa gituuu

# isalpha() <--- Utk mengecek semuanya huruf 
# isalnum() <--- Huruf dan angka (utk di password)
# isdecimal() <--- Angka saja 
# isspace() <--- Spasi, tab, newline \n 
# istitle() <--- Semua kata dimulai dg huruf besar

print("\nMengecek komponen menggunakan istitle()")
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # Hasilnya Bool
print(judul + " is title = " + str(cek_judul))

judul = "It's Okay Not To Be Orkay"  # Sebenarnya dlm menulis judul itu dilarang pakai astoprot atau tanda kutip (')
cek_judul = judul.istitle() # Hasilnya Bool
print(judul + " is title = " + str(cek_judul))

judul = "It is Okay Not To Be Orkay"  # Harus besar semuanya 
cek_judul = judul.istitle() # Hasilnya Bool
print(judul + " is title = " + str(cek_judul))
print("\n")


## Mengecek komponen startswith() endswith() <--- Keren
print("Mengecek komponen menggunakan startswith()") # startswith() = Awal kalimat
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("Start = " + str(cek_start))

cek_start = "Sangjangnim Oppa".startswith("sangjangnim")
print("Start = " + str(cek_start))
# (Sangjangnim) = harus sama apapun itu upper atau lower case nya

print("\nMengecek komponen menggunakan endswith()") # endswith() = akhir kalimat
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("End = " + str(cek_end))
cek_end = "Sangjangnim Oppak".endswith("Oppa")
print("End = " + str(cek_end))


## Penggabungan Komponen join() split()
print("\nPenggabungan Komponen")
pisah = ["Aku", "sayang", "kamu"]  # [] namanya List
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))
# join() kebalikan dari split()


## Alokasi Karakter rjust() ljust() center()
     # rjust() = Right Justify (Rata kanan)
     # ljust() = Left Justify (Rata Kiri)

print("\nAlokasi Karakter")
print(5 * "=" + "data" + "=" * 5)

print("\nKanan = rjust()")
kanan = "kanan".rjust(10)  # Rata kanan dg alokasi 10 
print("'" + kanan + "'")  # Viar kelihatan batas kanannya

kanan = "surotong".rjust(10)  # Rata kanan dg alokasi 10 
print("'" + kanan + "'")  # Viar kelihatan batas kanannya

print("\nKiri = ljust()")
kiri = "kiri".ljust(10)  # Rata kiri dg alokasi 10
print("'" + kiri + "'")  # Viar kelihatan batas kirinya

print("\nCenter = center()")
tengah = "tengah".center(10)  
print("'" + tengah + "'")  

tengah = "tengah".center(20,"-")  # Biar gak spasi
print("'" + tengah + "'")  

tengah = "tengah".center(20,"@")  # Biar gak spasi
print("'" + tengah + "'")

tengah = "tengah".center(20,":")  # Biar gak spasi
print("'" + tengah + "'")  

 
# Kebalikannya ---> strip()
print("\nKebalikannya menggunakan strip()")
tengah = tengah.strip(":")  # Menghilangkan yg sisa sisanya
print("'" + tengah + "'")  

kanan = kanan.strip(":")  # Menghilangkan tanda :
print("'" + kanan + "'")  


# Sebenarnya masih banyak Method dari pada yang di atas
# Setiap Method memiliki kegunaan
# Dipersilahkan utk mengeksplor sendiri 




print("\n")











































































































