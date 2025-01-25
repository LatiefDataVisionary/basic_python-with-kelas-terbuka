### MEMBUAT PACKAGE
print( "\n" + "=" * 10 + "MEMBUAT PACKAGE" + "=" * 10 + "\n")


import time

t_start = time.time()

import sains_lima_enam.matematika

hasil_tambah = sains_lima_enam.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah dari package adalah = {hasil_tambah}")
t_end = time.time()

print(f"Waktu eksekusi adalah = {t_end - t_start}")


print("\n====Modul Fisika====")
from sains_lima_enam import fisika
# atau jg bisa import sains_lima_enam.fisika

gaya = fisika.gaya(90, 10)
print(f"Gaya adalah = {gaya}")


from sains_lima_enam.fisika import gaya

gaya = gaya(90, 10)
print(f"Gaya adalah = {gaya}")


from sains_lima_enam.fisika import gaya as force

gaya = force(90, 10)
print(f"Gaya adalah = {gaya}")







































































































print("\n")