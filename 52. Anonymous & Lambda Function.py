### Anonymous & Lambada Function
print("\n" + "=" * 10 + "Anonymous & Lambda Function" + "=" * 10 + "\n")

## Lambda Function
# Membuat program menjadi lebih simple


def fungsi_kuadrat(angka):
    # print(angka ** 2)
    return angka ** 2 

# kuadrat(3)
print(fungsi_kuadrat(3))
print(f"Hasil fungsi kuadrat = {fungsi_kuadrat(3)}")


## Kita coba dg Lambda
print("\n===Kita coba dg Lambda")

# Output = Lambda Argument:Expression
kuadrat = lambda angka : angka ** 2

print(f"Hasil Lambda Kuadrat = {kuadrat(5)}")


pangkat = lambda num,pow : num ** pow
print(f"Hasil Lambda pangkat = {pangkat(4,2)}")


## Kegunaannya apa bang?
print("\n===Kegunaannya apa bang?")

# Sorting utk List biasa
print("\n--Sorting utk List biasa")

data_list = ["Otong","Ucup","Dudung"]
data_list.copy()  # sorting berdasarkan abcd
print(f"Sorted List = {data_list}")

# Sorting dia pakai panjang
print("\n--Sorting dia pakai panjang")

data_list.sort(key = len)
print(f"Sorted List by Len = {data_list}")

# Jika menggunakan fungsi (hasilnya tetap sama)
def panjang_nama(nama):
    return len(nama)
data_list.sort(key = panjang_nama)
print(f"Sorted List by Panjang = {data_list}")

# Sort pakai Lambda
print("\n--Sort pakai Lambda")

data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted List by Lambda = {data_list}")


## Filter 
print("\n--Filter")

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x:x < 5, data_angka))
print(data_angka_baru)

## Kasus genap
data_genap = list(filter(lambda x:(x % 2 == 0), data_angka))
print(data_genap)

## Kasus ganjil
data_ganjil = list(filter(lambda x:(x % 2 == 1), data_angka))
# atau
# data_ganjil = list(filter(lambda x:(x % 2 != 0), data_angka))
print(data_ganjil)

## Kelipatan 3 
data_3 = list(filter(lambda x:(x % 3 == 0), data_angka))
print(data_3)



## Anonymous Function
# Currying <-- Haskell Curry
print("\n===Anonymous Function")

def pangkat(angka,n):
    hasil = angka ** n
    return hasil
4
data_hasil = pangkat(5,2)
print(f"Function Biasa = {data_hasil}")

# Dengan Currying menjadi
print("---Dengan Currying menjadi")

def pangkat(n):
    return lambda angka:angka ** n

pangkat_2 = pangkat(2)
print(f"Pangkat 2 = {pangkat_2(5)}")

pangkat_3 = pangkat(3)
print(f"Pangkat 3 = {pangkat_3(3)}")
print(f"Pangkat Bebas = {pangkat(4)(5)}")














































































print("\n")