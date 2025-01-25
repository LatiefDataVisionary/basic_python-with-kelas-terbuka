# Latihan Komparasi dan Logika

# Membuat gabungan area rentang dari angka

# +++++++3-----------10+++++++++

print("\n")
inputUser = float(input("Masukkan angka yg bernilai kurang dari 3 atau lebih besar dari 10 : "))

# ++++++++3-------------------------
# Memeriksa angka kurang dari 3
isKurangDari= (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

# ----------------------10+++++++++++++
# Memeriksa angka lebih besar dari 10 
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)


# +++++++3-----------10+++++++++
# Kasus Gabungan 
isCorrect = isKurangDari or isLebihDari
print("Angka yg Anda masukkan: ", isCorrect)


# -------3++++++++++++10-------------
# Kasus Irisan
print("\n", 10 * "=", "\n")
inputUser = float(input("Masukkan angka yg bernilai lebih dari 3 dan kurang dari 10 : "))

# -----------3+++++++++++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# ++++++++++++10-------------
# Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

# -------3++++++++++++10-------------
isCorrect = isKurangDari and isLebihDari
print("Angka yg Anda masukkan: ", isCorrect)


#PR 

# 1. ------0+++++++5-------8++++++++11--------

print("\n")
print("\n1. ------0+++++++5-------8++++++++11--------")
print("Lebih besar dari 0 dan kurang dari 5")
lebih0_Kurang5 = input("Masukkan angka = ")
hasilLebih0_Kurang5 = 0 < float(lebih0_Kurang5) and float(lebih0_Kurang5) < 5 # Gunakan operator and dan <
# hasilLebih0_Kurang5 = 0 < float(lebih0_Kurang5) < 5 
print("Angka yg anda masukkan = ", hasilLebih0_Kurang5)

print("\n")
print("Lebih besar dari 8 dan kurang dari 11")
lebih18_Kurang11 = input("Masukkan angka = ")
hasilLebih8_Kurang11 = 8 < float(lebih18_Kurang11) and float(lebih18_Kurang11) < 11 
# hasilLebih8_Kurang11 = 8 < float(lebih0_Kurang5) < 11 
print("Angka yg anda masukkan = ", hasilLebih8_Kurang11)


# 2. ++++++0-------5+++++++8--------11++++++++

print("\n\n2. ++++++0-------5+++++++8--------11++++++++")
print("Lebih kecil dari 0")
lebihKecilDari_0 = input("Masukkan angka lebih kecil dari 0 = ")
hasil_LebihKecilDari_0 = int(lebihKecilDari_0) < 0 
print("angka yg anda masukkan = ", hasil_LebihKecilDari_0)

print("\n")
print("Lebih besar dari 5 dan kurang dari 8")
lebihBesar5_Kurang8 = input("Masukkan angka lebih besar dari 5 dan kurang dari 8 = ")
hasil_lebihBesar5_Kurang8 = 5 < int(lebihBesar5_Kurang8) and int(lebihBesar5_Kurang8) < 8
print("angka yg anda masukkan = ", hasil_lebihBesar5_Kurang8)

print("\n")
print("Lebih besar dari 11")
lebihBesarDari_11 = input("Masukkan angka lebih besar dari 11 = ")
hasil_LebihBesarDari_11 = int(lebihBesarDari_11) > 11 
print("angka yg anda masukkan = ", hasil_LebihBesarDari_11)




print("\n\n\n\t\tHOREEEEEE!!!!!")



































































































































