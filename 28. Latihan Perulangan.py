# Latihan Perulangan Membuat Segitiga
from ast import Continue


print("\n" + 10 * "=" + "Latihan Perulangan" + "=" * 10 + "\n")

# Segitiga Siku Siku
print("=" * 4 + "Segitiga Siku - siku" + "=" * 4 + "\n")
sisi = 10

# 1. Menggunakan For
# Dummy Variable
print("=" * 2 + "1. Menggunakan For" + "=" * 2 + "\n")
print("=" * 2 + "Dummy Variable" + "=" * 2 + "\n")
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1

# 2. Menggunakan While
print("=" * 2 + "2. Menggunakan While" + "=" * 2 + "\n")
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

print("Akhir dari While\n")


# 3. Hanya ganjil saja
print("=" * 2 + "3. Hanya ganjil saja" + "=" * 2 + "\n")
count = 1
while True:
    if ~(count % 2):
        # Print jika Ganjil
        print("*" * count)
        count += 1
    else :
        # Print jika Genap
        count += 1
        continue

    # Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir dari While\n")


count = 1
spasi = int(sisi/2)
while True:
    if (count % 2):
        # Print jika Ganjil
        print(" " * spasi ,"+" * count)
        spasi -= 1
        count += 1
    else :
        # Print jika Genap
        count += 1
        continue

    # Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir dari While\n")












































































































































































print("\n")