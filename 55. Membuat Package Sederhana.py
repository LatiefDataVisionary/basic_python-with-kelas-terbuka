### MEMBUAT PACKAGE SEDERHANA
print("\n" + "=" * 10 + "MEMBUAT PACKAGE SEDERHANA" + "=" * 10)


## Main App
print("\n====Main App")
## Module matematika dg Import

import matematika_lima_lima 

hasil_tambah = matematika_lima_lima.tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali= matematika_lima_lima.kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = matematika_lima_lima.pangkat(3)
print(f"Hasil pangkat 3 = {pangkat_3(3)}")


## Main Form
print("\n====Main From")

from matematika_lima_lima import tambah, kali
from matematika_lima_lima import *  # Mengambil semua fungsi di matematika_lima_lima
# tp lebih direkomendasiin utk pakai yg atas

hasil_tambah = tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"Hasil tambah = {hasil_kali}")

pangkat_3 = matematika_lima_lima.pangkat(3)
print(f"Hasil pangkat 3 = {pangkat_3(3)}")


## Main Alias
print("\n====Main Alias")

from matematika_lima_lima import tambah as add
from matematika_lima_lima import kali as k
from matematika_lima_lima import pangkat as terserah_kalian_mau_apa

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = k(1,2,3,4,5)
print(f"Hasil tambah = {hasil_kali}")

pangkat_3 = terserah_kalian_mau_apa(3)
print(f"Hasil pangkat 3 = {pangkat_3(3)}")


import matematika_lima_lima as math  # <--- bisa dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"Hasil tambah = {hasil_kali}")

pangkat_3 = terserah_kalian_mau_apa(3)
print(f"Hasil pangkat 3 = {pangkat_3(3)}")





















































































print("\n")