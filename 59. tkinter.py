# GUI -->> Graphical User Interface

import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!!")

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    # print(NAMA_BELAKANG.get())
    # pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, gantengKuuuu!!!"
    pesan = f"El kok ganteng banget ya!!!!!! AWWWWWWWW!!!1111"
    showinfo(title="Whatuppp!!",message=pesan)

# frame input 
input_frame = ttk.Frame(window)

# penempatan Grid, Pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen 
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. entry nama depan 
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry nama belakang 
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

# 5. Tombol 
tombol_sapa = ttk.Button(input_frame,text="Sapa!!",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)


# Main Loop Window
window.mainloop()






# class Stack:
#     def __init__(self, jmlh_max=100):  #ditentukan max arraynya 100
#         self.stack = [None] * jmlh_max  
#         self.top = -1
#         self.jmlh_max = jmlh_max

#     def push(self, nilai):
#         if self.top >= self.jmlh_max - 1:
#             print("Mohon maaf, Stack penuh!")
#         else:
#             self.top += 1
#             self.stack[self.top] = nilai
#             print(f"{nilai} ditambahkan ke stack.")
#             if self.top == self.jmlh_max - 2:  # ini utk (sel.top) index ke 3 = 3 utk (jmlh_max(5) - 2)---> 5-2=3
#                 print("Peringatan: Stack hampir penuh.")

#     def pop(self):
#         if self.top < 0:
#             print("Stack kosong!")
#         else:
#             nilai = self.stack[self.top]
#             self.stack[self.top] = None  # Hapus nilai
#             self.top -= 1
#             print(f"{nilai} dihapus dari stack.")

#     def replace(self, index, nilai):
#         if index < 0 or index > self.top:
#             print("Indeks tidak valid!")
#         else:
#             self.stack[index] = nilai
#             print(f"Nilai pada indeks {index} diganti dengan {nilai}.")

#     def display(self):
#         if self.top < 0:
#             print("Stack kosong.")
#         else:
#             print("Elemen-elemen dalam stack adalah:", end=" ")
#             for i in range(self.top, -1, -1):
#                 print(self.stack[i], end=" ")
#             print()

# def main():
#     jmlh_max = int(input("Masukkan ukuran maksimum stack (hingga 100): "))
#     if jmlh_max > 100:
#         jmlh_max = 100
#         print("Mohon Maaf, ukuran maksimum dibatasi menjadi 100.")
#     stack = Stack(jmlh_max)

#     while True:
#         print("\nOperasi Stack")
#         print("1. Tambah (Push)")
#         print("2. Hapus (Pop)")
#         print("3. Ganti (Replace)")
#         print("4. Tampilkan (Display)")
#         print("5. Keluar")
#         pilihan = int(input("Masukkan pilihan Anda: "))

#         if pilihan == 1:
#             nilai = int(input("Masukkan nilai untuk ditambahkan: "))
#             stack.push(nilai)
#         elif pilihan == 2:
#             stack.pop()
#         elif pilihan == 3:
#             index = int(input("Masukkan indeks untuk diganti (indeks mulai dari 0): "))
#             nilai = int(input("Masukkan nilai baru: "))
#             stack.replace(index, nilai)
#         elif pilihan == 4:
#             stack.display()
#         elif pilihan == 5:
#             print("Keluar...")
#             break
#         else:
#             print("Pilihan tidak valid! Silakan masukkan pilihan yang valid.")

# if __name__ == "__main__":
#     main()








# class Stack:
#     def __init__(self, jmlh_max=100):
#         self.stack = [None] * jmlh_max 
#         self.top = -1
#         self.jmlh_max = jmlh_max

#     def push(self, nilai):
#         if self.top >= self.jmlh_max - 1:
#             print("┌" + "─" * 15 + "┐")
#             print("│ Stack penuh! │")
#             print("└" + "─" * 15 + "┘")
#         else:
#             self.top += 1
#             self.stack[self.top] = nilai
#             print("┌" + "─" * 35 + "┐")
#             print(f"│ {nilai} ditambahkan ke stack. │")
#             print("└" + "─" * 35 + "┘")
#             if self.top == self.jmlh_max - 2:
#                 print("┌" + "─" * 35 + "┐")
#                 print("│ Peringatan: Stack hampir penuh. │")
#                 print("└" + "─" * 35 + "┘")

#     def pop(self):
#         if self.top < 0:
#             print("┌" + "─" * 15 + "┐")
#             print("│ Stack kosong! │")
#             print("└" + "─" * 15 + "┘")
#         else:
#             nilai = self.stack[self.top]
#             self.stack[self.top] = None  # Hapus nilai
#             self.top -= 1
#             print("┌" + "─" * 35 + "┐")
#             print(f"│ {nilai} dihapus dari stack. │")
#             print("└" + "─" * 35 + "┘")

#     def replace(self, index, nilai):
#         if index < 0 or index > self.top:
#             print("┌" + "─" * 20 + "┐")
#             print("│ Indeks tidak valid! │")
#             print("└" + "─" * 20 + "┘")
#         else:
#             self.stack[index] = nilai
#             print("┌" + "─" * 40 + "┐")
#             print(f"│ Nilai pada indeks {index} diganti dengan {nilai}. │")
#             print("└" + "─" * 40 + "┘")

#     def display(self):
#         if self.top < 0:
#             print("┌" + "─" * 15 + "┐")
#             print("│ Stack kosong. │")
#             print("└" + "─" * 15 + "┘")
#         else:
#             print("┌" + "─" * 35 + "┐")
#             print("│ Elemen-elemen dalam stack adalah: │")
#             print("├" + "─" * 35 + "┤")
#             for i in range(self.top, -1, -1):
#                 print(f"│ {self.stack[i]} │")
#             print("└" + "─" * 35 + "┘")

# def main():
#     print("┌" + "─" * 35 + "┐")
#     print("│ Selamat datang di Program Stack! │")
#     print("└" + "─" * 35 + "┘")
    
#     jmlh_max = int(input("Masukkan ukuran maksimum stack (hingga 100): "))
#     if jmlh_max > 100:
#         jmlh_max = 100
#         print("┌" + "─" * 35 + "┐")
#         print("│ Ukuran maksimum diatur menjadi 100. │")
#         print("└" + "─" * 35 + "┘")
#     stack = Stack(jmlh_max)

#     while True:
#         print("\n┌" + "─" * 35 + "┐")
#         print("│ Operasi Stack │")
#         print("├" + "─" * 35 + "┤")
#         print("│ 1. Tambah (Push) │")
#         print("│ 2. Hapus (Pop) │")
#         print("│ 3. Ganti (Replace) │")
#         print("│ 4. Tampilkan (Display) │")
#         print("│ 5. Keluar │")
#         print("└" + "─" * 35 + "┘")
        
#         pilihan = int(input("Masukkan pilihan Anda: "))

#         if pilihan == 1:
#             nilai = int(input("Masukkan nilai untuk ditambahkan: "))
#             stack.push(nilai)
#         elif pilihan == 2:
#             stack.pop()
#         elif pilihan == 3:
#             index = int(input("Masukkan indeks untuk diganti (indeks mulai dari 0): "))
#             nilai = int(input("Masukkan nilai baru: "))
#             stack.replace(index, nilai)
#         elif pilihan == 4:
#             stack.display()
#         elif pilihan == 5:
#             print("┌" + "─" * 15 + "┐")
#             print("│ Keluar... │")
#             print("└" + "─" * 15 + "┘")
#             break
#         else:
#             print("┌" + "─" * 35 + "┐")
#             print("│ Pilihan tidak valid! Silakan masukkan pilihan yang valid. │")
#             print("└" + "─" * 35 + "┘")

# if __name__ == "__main__":
#     main()















































