# Episode INPUT USER

# Data yang dimasukkan pasti STRING
data = input("Masukkan data = ")
print("Data= ", data, ", Bertipe= ", type(data))

# Jika kita ingin mengambil INT dan FLOAT, maka 
data_int = int(input("Masukkan angka = "))
print("Data= ", data_int, ", Bertipe = ", type(data_int))

data_float = float(input("Masukkan angka = "))
print("Data= ", data_float, ", Bertipe = ", type(data_float))

# Bagaimana dengan BOOLEAN
biner = bool(input("Masukkan boolean = "))
print("Data = ", biner,", Bertipe = ", type(biner))

biner = bool(int(input("Masukkan boolean = "))) # Agar bisa memunculkan FALSE jika menginputkan 0
print("Data = ", biner,", Bertipe = ", type(biner))







