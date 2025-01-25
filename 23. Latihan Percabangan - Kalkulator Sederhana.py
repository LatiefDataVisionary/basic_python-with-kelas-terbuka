# Latihan Percabangan - Kalkulator Sederhana
print("\n" + "=" *6 + "Latihan Percabangan - Kalkulator Sederhana" + "=" * 6 + "\n")

print("=" * 20)
print("Kalkulator Sederhana")
print("=" * 20 + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
angka_2 = float(input("Masukkan angka 2 = "))
operator = input("Operator (+,-,x,/) = ")

# Percabangannya
if operator == "+":
    hasil = angka_1 + angka_2 
    print("Hasilnya adalah = ", hasil)
elif operator == "-":
    hasil = angka_1 - angka_2 
    print("Hasilnya adalah = ", hasil)
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2 
    print("Hasilnya adalah = ", hasil)
elif operator == "/":
    hasil = angka_1 / angka_2 
    print("Hasilnya adalah = ", hasil)
else:
    print("Silahkan masukkan operator yang telah disediakan")


print("Akhir dari program, terima gajih!")





























































































































































print("\n")