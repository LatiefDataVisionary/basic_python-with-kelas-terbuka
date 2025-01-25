print("Hello World")
a = 23

print("Nilaiku adalah: ", a)

for i in range(1,1):
    print("Cantik")
    
#Tipe Data Integer
aku = 50
print("Berapa nilaiku: ", aku)
print("Bertipe: ", type(aku))

#Tipe Data Float
dia = 23.45
print("Nilainya adalah: ", dia)
print("Bertipe: ", type(dia))

#Tipe Data String = Kumpulan karakter
DataString = "Latief"
DataString2 = "Yusuf 234"

print("Namaku adalah ", DataString)
print("Bertipe: ", type(DataString))
DataString = "Latief"
print("Namaku adalah ", DataString2)
print("Bertipe: ", type(DataString2))

#Tipe Data Biner/Boolean = True/False
DataBiner = True

print("Apakah True atau False? ", DataBiner)
print("Bertipe: ", type(DataBiner))

#Tipe Data Khusus 

#Bil. Kompleks
dataKompleks = complex(5,6)

print("Namaku adalah ", dataKompleks)
print("Bertipe: ", type(dataKompleks))

# #Tipe Data dari bahasa C
# from ctypes import c_double, c_char_p, c_char, c_long

# data_C_Double = c_double(10.5)
# data_C_Char_P = c_char_p(b"Hehehe")
# data_C_Char = c_char("H")
# data_C_Long = c_long(10)

# print("Data: ", data_C_Double)
# print("Bertipe: ", type(data_C_Double))

# print("Data: ", data_C_Char_P)
# print("Bertipe: ", type(data_C_Char_P))

# print("Data: ", data_C_Char)
# print("Bertipe: ", type(data_C_Char))

# print("Data: ", data_C_Long)
# print("Bertipe: ", type(data_C_Long))


#Tipe Data dari bahasa C
from ctypes import c_double, c_char_p, c_char, c_long

data_C_Double = c_double(10.5)
data_C_Char_P = c_char_p(b"Hehehe")
data_C_Char = c_char(b"H")
data_C_Long = c_long(10)

print("Data: ", data_C_Double)
print("Bertipe: ", type(data_C_Double))

print("Data: ", data_C_Char_P)
print("Bertipe: ", type(data_C_Char_P))

print("Data: ", data_C_Char)
print("Bertipe: ", type(data_C_Char))

print("Data: ", data_C_Long)
print("Bertipe: ", type(data_C_Long))

