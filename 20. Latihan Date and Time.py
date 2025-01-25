# Date and Time (Latihan)
print("\n" + "=" * 6 + "Date and Time (Latihan)" + "=" * 6 + "\n")

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")   # %A untuk harinya

tanggal = dt.date(2005,10,10)   # (yyyy,mm,dd)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")   # %A untuk harinya

print("\n" + "=" * 10)

print("Silahkan masukkan tanggal, \nbulan, dan tahun lahir Anda\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

print("\n")

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")  # Utk memunculkan hari 

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365       # '//' = Left Division
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Harinya adalah : {tanggal_lahir:%A}")   
print(f"Umur Anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")













































































































































print("\n")