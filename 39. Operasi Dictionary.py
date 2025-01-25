### Operasi Dictionary
print("\n" + "=" * 10 + "Operasi Dictionary" + "=" * 10 + "\n")

data_dict = {
    "cup":"Ucup Surucup",
    "tong":"Otong Surotong",
    "dung":"Dudung Surudung"
}

## Panjang Dictionary
print("--Panjang Dictionary--")
LENDICT = len(data_dict)
print(f"Panjang Dictionary = {LENDICT}")

## Mengecek Key exist atau tidal
print("\n--Mengecek Key exist atau tidak--")
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict?: {CHECKKEY}")

KEY = "kis"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict?: {CHECKKEY}")


## Mengakses Value (read) dengan Get
print("\n--Mengakses Value (read) dengan Get--")

print(data_dict["cup"])
# bila memasukkan nama Key yg gak ada maka error

print(data_dict.get("cup"))
print(data_dict.get("kis"))
print(data_dict.get("kis","Key tdk ditemukan!"))  # Utk mengganti kata "none"
# Get = tdk error ketika memasukkan nama Key yg tdk ada, diganti dengan tulisan "none"


## Mengupdate Data
print("\n--Mengupdate Data--")

data_dict["cup"] = "Ucup si Ganteng"  # Mengubah Value
print(data_dict)

data_dict["sep"] = "Asep si Kasyep"  # Menambah data
print(data_dict)

data_dict.update({"cup":"Ucup Surucup"})  # Mengedit value
print(data_dict)

data_dict.update({"Faqih":"Faqihzah"})
print(data_dict)

# Kesimpulannya : Bila ketemu data/key yg exist, maka dia akan mengedit value data tersebut
#                 Kalau key nya gk ada, maka dia akahn menambah secara otomatis 


## Delete data pada Dictionary
print("\n--Delete data pada Dictionary--")

del data_dict["Faqih"]
print(data_dict)


























































































print("\n")