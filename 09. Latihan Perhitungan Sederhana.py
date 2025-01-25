# Latihan Konversi Satuan Temperature

# Program Suhu/Temperature
"""
                Celcius     Reamur     Fahrenheit    Kelvin
    Celcius                  4/5 C      9/5 C+32      C+273
    Reamur       5/4 R                  9/4 R+32    5/4 K+273
    Fahrenheit  5/9(F-32)  4/5(F-32)                   PR
    Kelvin       k-273     4/5(K-273)     PR
"""

# Program Konversi CELCIUS ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input("Masukkan suhu dalam Celcius = "))
print("Suhu adalah ", celcius, "Celcius")

# REAMUR
reamur = (4/5) * celcius
print("Suhu adalah ", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
fahrenheit_2 = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah ", fahrenheit, "Fahrenheit")
print("Suhu dalam Fahrenheit adalah ", fahrenheit_2, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah ", kelvin, "Kelvin")


# PR 

# 1. Konversi Fahrenheit ke Kelvin
print("\n\t\t\t====PROGRAM RUMUS FAHRENHEIT KE KELVIN====\n")
fahrenheit = input("\t\t\tMasukkan suhu Fahrenheit = ")
celcius = 5/9 * (float(fahrenheit) - 32) # Ubah tipe data fahrenheit menjadi float
kelvin = celcius + 273
print("\t\t\tSuhu dari Fahrenheit ke Kelvin adalah ", kelvin)

# 2. Konversi Kelvin ke Fahrenheit
print("\n\n\t\t\t====PROGRAM RUMUS KELVIN KE FAHRENHEIT====\n")
kelvin = input("\t\t\tMasukkan suhu Kelvin = ")
celcius = (float(kelvin) - 273)
fahrenheit = 9/5 * (float(celcius) + 32)
print("\t\t\tSuhu dari Kelvin ke Fahrenheit adalah ", fahrenheit)
print("\n\n")


"""
                Celcius     Reamur     Fahrenheit    Kelvin
    Celcius                  4/5 C      9/5 C+32      C+273
    Reamur       5/4 R                  9/4 R+32    5/4 K+273
    Fahrenheit  5/9(F-32)  4/5(F-32)                   PR
    Kelvin       k-273     4/5(K-273)     PR
"""

# Cuma iseng iseng aja 
# Dari Celcius 
print("\n\n\t\t\t====PROGRAM RUMUS CELCIUS KE REAMUR====\n")
celcius = input("\t\t\tMasukkan suhu Celcius = ")
reamur = 4/5 * float(celcius)
print("\t\t\tSuhu dari Celcius ke Reamur adalah ", reamur)

print("\n\n\t\t\t====PROGRAM RUMUS CELCIUS KE FAHRENHEIT====\n")
celcius = input("\t\t\tMasukkan suhu Celcius = ")
fahrenheit = 9/5 * float(celcius) + 32
print("\t\t\tSuhu dari Celcius ke Fahrenheit adalah ", fahrenheit)

print("\n\n\t\t\t====PROGRAM RUMUS CELCIUS KE KELVIN====\n")
celcius = input("\t\t\tMasukkan suhu Celcius = ")
kelvin = int(celcius) + 273
print("\t\t\tSuhu dari Celcius ke Kelvin adalah ", kelvin)


# Dari Reamur
print("\n\n\t\t\t====PROGRAM REAMUR KE CELCIUS====\n")
reamur = input("\t\t\tMasukkan suhu Reamur = ")
celcius = 5/4 * float(reamur)
print("\t\t\tSuhu dari Reamur ke Celcius adalah ", celcius)

print("\n\n\t\t\t====PROGRAM REAMUR KE ====\n")
reamur = input("\t\t\tMasukkan suhu Reamur = ")
fahrenheit = 9/4 * float(reamur) + 32 
print("\t\t\tSuhu dari Reamur ke Fahrenheit adalah ", fahrenheit)

print("\n\n\t\t\t====PROGRAM REAMUR KE KELVIN====\n")
reamur = input("\t\t\tMasukkan suhu Reamur = ")
kelvin = 5/4 * float(reamur) + 273
print("\t\t\tSuhu dari Reamur ke Fahrenheit adalah ", kelvin)

# Dari Fahrenheit 
print("\n\n\t\t\t====PROGRAM FAHRENHEIT KE CELCIUS====\n")
fahrenheit = input("\t\t\tMasukkan suhu Fahrenheit = ")
celcius = 5/9 * float(fahrenheit-32)
print("\t\t\tSuhu dari Fahrenheit ke Celcius adalah ", celcius)

print("\n\n\t\t\t====PROGRAM FAHRENHEIT KE REAMUR====\n")
fahrenheit = input("\t\t\tMasukkan suhu Fahrenheit = ")
reamur = 4/5 * float(fahrenheit-32) 
print("\t\t\tSuhu dari Fahrenheit ke Reamur adalah ", reamur)

# Dari Kelvin 
print("\n\n\t\t\t====PROGRAM KELVIN KE CELCIUS====\n")
kelvin = input("\t\t\tMasukkan suhu Fahrenheit = ")
celcius = int(kelvin-273)
print("\t\t\tSuhu dari Kelvin ke Celcius adalah ", celcius)

print("\n\n\t\t\t====PROGRAM KELVIN KE REAMUR====\n")
kelvin = input("\t\t\tMasukkan suhu Fahrenheit = ")
reamur = 4/5 * float(kelvin-273)  
print("\t\t\tSuhu dari Kelvin ke Reamur adalah ", reamur)

print("\n\n")








