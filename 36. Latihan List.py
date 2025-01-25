# Latihan List
print("\n" + "=" * 10 + "Latihan List" + "=" * 10)

# Membuat Database Sederhana Menggunakan List
# Membuat daftar buku = Penulisnya, judulnya
# Program List Buku
print("\n" + "-" * 3 + 'Program List Buku' + "-" * 3 + "\n")

# Menggunakan Nesting List

list_buku = []
while True:
    print("Masukkan Data Buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    print(list_buku)

    print("\n\n", "=" * 10 + "Data Buku" + "=" * 10)
    print("No. | Judul| Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} |{buku[0]} | {buku[1]}")
    
    print("\n\n", "=" * 20)
    isLanjut = input("Apakah dilanjutkan?(y/n) : ")
    
    if isLanjut == "n":
        break

print("PROGRAM SELESAI!")






























































































































print("\n")