# Kita belajar CASTING
# Merubah dari sutau tipe ke tipe yang lain 
# Tipe data = int, float, mstr, bool

# Tipe Data Int
data_int = 2
print("Data = ", data_int, ", Bertipe =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan False jika nnilai integer atau angka = 0

print("Data = ", data_float, ", Bertipe =", type(data_float))
print("Data = ", data_str, ", Bertipe =", type(data_str))
print("Data = ", data_bool, ", Bertipe =", type(data_bool))


# Tipe Data Float
print("\n=====FLOAT====")
data_float = 9.5
print("Data = ", data_float, ", Bertipe =", type(data_float))

data_int = int(data_float) # Akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan False jika nilai float = 0

print("Data = ", data_int, ", Bertipe =", type(data_int))
print("Data = ", data_str, ", Bertipe =", type(data_str))
print("Data = ", data_bool, ", Bertipe =", type(data_bool))


# Tipe Data Boolean
print("=====BOOLEAN====")
data_bool = True
print("Data = ", data_bool, ", Bertipe =", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool) 

print("Data = ", data_int, ", Bertipe =", type(data_int))
print("Data = ", data_str, ", Bertipe =", type(data_str))
print("Data = ", data_float, ", Bertipe =", type(data_float))


# Tipe Data String
print("=====STRING====")
data_str = "10"
print("Data = ", data_str, ", Bertipe =", type(data_str))

data_int = int(data_str) 
data_float = float(data_str) 
data_bool = bool(data_str)

print("Data = ", data_int, ", Bertipe =", type(data_int))
print("Data = ", data_float, ", Bertipe =", type(data_float))
print("Data = ", data_bool, ", Bertipe =", type(data_bool))







