# Continue, Pass dan Break 
print("\n" + 10 * "=" + "Continue, Pass, dan Break" + 10 * "=" + "\n")

# Pass berfungsi sbg Dummy, tdk akan di eksekusi

angka = 0 
while angka < 5:
    angka += 1
    if angka == 3:
        print("Whadaap!!")
    print(angka)

print("\n")

angka = 0 
while angka < 5:
    angka += 1
    if angka == 3:
        pass  # Ini tdk akan dieksekusi
    print(angka)

def fungsi():
    pass  # Gak di aktifkan

class hero:
    pass  # Fungsi ini ada tapi tidak di implementasikan


# Continue 
print("\n" + "=" * 4 + "Continue" + "=" * 4 + "=" + "\n")

angka = 0
print(f"Angka sekarang --> {angka}\n")

while angka < 5:
    angka += 1
    print(f"Angka sekarang ---> {angka}")
    print("Whaaasuuuup!!!!")

print("Nice!!!")    


angka = 0
print(f"Angka sekarang --> {angka}\n")

while angka < 5:
    angka += 1
    print(f"Angka sekarang ---> {angka}")

    if angka == 3:
        print("Nice")
    print("Whaaasuuuup!!!!")

print("PINISHHH!!!") 

angka = 0
print(f"Angka sekarang --> {angka}\n")

while angka < 5:
    angka += 1
    print(f"Angka sekarang ---> {angka}")

    if angka == 3:
        print("Nice")
        continue  # Akan membuat Loop meloncat ke loop berikutnya
    print("Whaaasuuuup!!!!")  # Aksi 2

print("PINISHHH!!!")



































































































print("\n")