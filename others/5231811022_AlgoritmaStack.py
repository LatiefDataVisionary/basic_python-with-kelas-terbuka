class Stack:
    def __init__(self, jmlh_max=100):  #ditentukan max arraynya 100
        self.stack = [None] * jmlh_max  
        self.top = -1
        self.jmlh_max = jmlh_max

    def push(self, nilai):
        if self.top >= self.jmlh_max - 1:
            print("Mohon maaf, Stack penuh!")
        else:
            self.top += 1
            self.stack[self.top] = nilai
            print(f"{nilai} ditambahkan ke stack.")
            if self.top == self.jmlh_max - 2:  # ini utk (sel.top) index ke 3 = 3 utk (jmlh_max(5) - 2)---> 5-2=3
                print("Peringatan: Stack hampir penuh.")

    def pop(self):
        if self.top < 0:
            print("Stack kosong!")
        else:
            nilai = self.stack[self.top]
            self.stack[self.top] = None  # Hapus nilai
            self.top -= 1
            print(f"{nilai} dihapus dari stack.")

    def replace(self, index, nilai):
        if index < 0 or index > self.top:
            print("Indeks tidak valid!")
        else:
            self.stack[index] = nilai
            print(f"Nilai pada indeks {index} diganti dengan {nilai}.")
            if index == self.top:
                while self.top >= 0 and self.stack[self.top] is None:
                    self.top -= 1
            print(f"Indeks teratas sekarang: {self.top}")
            self.display() 


    def display(self):
        if self.top < 0:
            print("Stack kosong.")
        else:
            print("Elemen-elemen dalam stack adalah:", end=" ")
            for i in range(self.top, -1, -1):
                if self.stack[i] is not None:  
                    print(self.stack[i], end=" ")
            print()


def main():
    jmlh_max = int(input("Masukkan ukuran maksimum stack (hingga 100): "))
    if jmlh_max > 100:
        jmlh_max = 100
        print("Mohon Maaf, ukuran maksimum dibatasi menjadi 100.")
    stack = Stack(jmlh_max)

    while True:
        print("\nOperasi Stack")
        print("1. Tambah (Push)")
        print("2. Hapus (Pop)")
        print("3. Ganti (Replace)")
        print("4. Keluar")
        pilihan = int(input("Masukkan pilihan Anda: "))

        if pilihan == 1:
            nilai = int(input("Masukkan nilai untuk ditambahkan: "))
            stack.push(nilai)
        elif pilihan == 2:
            stack.pop()
        elif pilihan == 3:
            stack.display() 
            index = int(input("Masukkan indeks untuk diganti (indeks mulai dari 0, dari kanan): "))
            nilai = int(input("Masukkan nilai baru: "))
            stack.replace(index, nilai)
        elif pilihan == 4:
            print("Program selesai...")
            break
        else:
            print("Nomor tidak valid! Silakan masukkan angka yang valid.")


if __name__ == "__main__":
    main()