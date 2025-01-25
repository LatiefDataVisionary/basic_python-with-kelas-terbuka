# OPERASI ARITMATIKA
print("\n" + "=" * 6 + "OPERASI ARTIMATIKA" + "=" * 6)
a = 6
b = 2

# Operasi Penjumlahan +
print("\n" + "=" * 4 + "Operasi Penjumlahan" + "=" * 4)
hasil = a + b

print("Hasilnya adalah ", hasil)
print('Atau ', a,'+', b,'=', hasil)


# Operasi Pengurangan -
print("\n" + "=" * 4 + "Operasi Pengurangan" + "=" * 4)
hasil = a - b
print("Hasilnya adalah ", hasil)
print('Atau ', a,'-', b,'=', hasil)


# Operasi Perkalian *
print("\n" + "=" * 4 + "Operasi Perkalian" + "=" * 4)
hasil = a * b
print("Hasilnya adalah ", hasil)
print('Atau ', a,'*', b,'=', hasil)


# Operasi Pembagian /
print("\n" + "=" * 4 + "Operasi Pembagian" + "=" * 4)
hasil = a / b
print("Hasilnya adalah ", hasil)
print('Atau ', a,'/', b,'=', hasil)


# Operasi Eksponen (Pangkat) **
print("\n" + "=" * 4 + "Operasi Eksponen (Pangkat)" + "=" * 4)
hasil = a ** b
print("Hasilnya adalah ", hasil)
print('Atau ', a,'**', b,'=', hasil)


# Operasi Modullus (Sisa Pembagian) %
print("\n" + "=" * 4 + "Operasi Modullus (Sisa Pembagian)" + "=" * 4)
hasil = a % b
print("Hasilnya adalah ", hasil)
print('Atau ', a,'%', b,'=', hasil)


# Operasi Floor Division (Kebalikan dari Modullus) //
print("\n" + "=" * 4 + "Operasi Floor Division (Kebalikan dari Modullus)" + "=" * 4)
hasil = a // b
print("Hasilnya adalah ", hasil)
print('Atau ', a,'//', b,'=', hasil)
print("\n")

# Prioritas Operasi, Operational Precedence
"""
     1. ()
     2. Eksponen **
     3. Perkalian dan teman teman * / ** % //
     4. Pertambahan dan Pengurangan + -
"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print("Hasilnya adalah = ", hasil)
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=", hasil)






































