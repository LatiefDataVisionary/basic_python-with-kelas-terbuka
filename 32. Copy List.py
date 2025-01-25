# Copy List 
# bagaimana kelakuan copy dari list
print("\n" + "=" * 10 + "Copy List" + "=" * 10 + "\n")


a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a  # Ini sebenarnya bkn mencopy
# Atau hanya membuat list dg nama lain tp Address nya sama
# Disebut Pass by Reference (a memberikan Reference ke si b)
print(f"b = {b}")

# Kita akan merubah member dari a 
print("\n# Kita akan merubah member dari a ")
print("\n")
a[1] = "Michael"
print(f"a = {a}")
print(f"b = {b}")

# Ini akan merubah kedua List
print("\n# Ini akan merubah kedua List")
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")


# Address dari kedua list a dan b
print("\n# Address dari kedua list a dan b")
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}")

"""
    References utk List
list a ---> [Address ("Ucup", "Otong", "Dudung")]
b = a ---> list b mengambil address yg sama dg list a 
list b membuat atau menduplikat data list a 

c = a.copy() ---> Membuat List baru dg Address yg berbeda
                  Sehingga mendptkan data yg sama dg List a


"""


# Menduplikat List dg Copy
print("\n# Menduplikat List dg Copy")
print("Membuat List C dg a.copy()")
c = a.copy()  # Full Duplikat/data baru (dia akan membuat data baru)
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}")
print(f"Address c = {hex(id(c))}\n")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}\n")

print("Kita ubah data 0")
c[0] = "Dadang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}\n")

print("Kita ubah data 1")
a[1] = "Otong"
print(f"a = {a}")
print(f"b = {b}")  # Outputnya list a dan list b berubah karena satu Address
print(f"c = {c}\n")  # Yg list c engga krn beda address






















































































































print("\n")