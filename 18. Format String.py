# Format String 
print("18. Format String")

# Contoh Generic 
# String
print("Contoh Generic")
print("String")
nama ="marlene"
str = "hello " + nama + ", apa kabar?"
print(str)

nama ="marlene"
format_str = f"hello {nama}"
print(format_str)

nama ="ucup"
format_str = f"hello {nama}"
print(format_str)


# Boolean
print("\nBoolean")
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

boolean = False
format_str = f"boolean = {boolean}"
print(format_str)


# Angka
print("\nAngka")
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)


# Bilangan Bulat 
print("\nBilangan Bulat")
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

angka = 15.77
format_str = f"bilangan bulat = {angka:f}"
print(format_str)

# Bilangan dg Ordo Ribuan
print("\nBilangan Ribuan")
angka = 2000
format_str = f"ribuan = {angka}"
print(format_str)

angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# Bilangan Desimal
print("\nBilangan Desimal")
angka = 2005.5
format_str = f"desimal = {angka}"
print(format_str)

angka = 2005.54321
format_str = f"desimal = {angka}"
print(format_str)

angka = 2005.54321
format_str = f"desimal = {angka:.2f}"  # Utk memunculkan 2 angka setelah koma
print(format_str)

# Menampilkan Leading Zero atau didepannya
print("\nMenampilkan Leading Zero")
angka = 2005.54321
format_str = f"desimal = {angka:8.3f}"  # Totalnya adalah 8 
print(format_str)

angka = 2005.54321
format_str = f"desimal = {angka:9.3f}"  # Totalnya adalah 8, menggeser 
print(format_str)

angka = 2005.54321
format_str = f"desimal = {angka:09.3f}"  # Menambahkan yg kosong menjadi 0
print(format_str)

angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"  # Menambahkan yg kosong menjadi 0
print(format_str)

# Menampilkan tandav + atau -
print("\nMenampilkan tanda + atau -")
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus}"
print(format_minus)
print(format_plus)

angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"  # Utk menampilkan tanda +
print(format_minus)
print(format_plus)

angka_minus = -10
angka_plus = -10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# Menformat Perse (%)
print("\nMenformat Persen (%)")
persentase = 0.045
format_persen  = f"persen = {persentase}"
print(format_persen)

persentase = 0.045
format_persen  = f"persen = {persentase:2%}"
print(format_persen)

persentase = 0.045
format_persen  = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan Operasi Aritmatika didlm placeholder ({})
print("\nMelakukan Operasi Aritmatika didalam placeholder ({})")
harga = 10000
jumlah = 5
format_string = f"harga total = {harga * jumlah}"
print(format_string)

harga = 10000
jumlah = 5
format_string = f"harga total = {harga * jumlah:,}"  # Pakai koma
print(format_string)

harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga * jumlah:,}"  # Pakai koma
print(format_string)


# Format angka lain (binary, octal, hexadecimal)
print("\nFormat angka lain (binary, octal, hexadecimal)")
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex  = f"hex = {hex(angka)}"
print("angka = ", angka)
print(format_binary)
print(format_octal)
print(format_hex)



























print("\n")










































































































































