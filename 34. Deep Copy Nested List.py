# Deep Copy Nested List
print("\n" + "=" * 10 + "Deep Copy Nested List" + "=" * 10 + "\n")
data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1]

data_2D_copy = data_2D.copy()

print(f"Data = {data_2D}")
print(f"Data Copy = {data_2D_copy}")

# Mengambil Data utk Nested List
print("\n" + "=" * 3 + "Mengambil Data utk Nested List" + "=" * 3)
data = data_2D[0]
print(f"Data = {data}")

data = data_2D[0][0]  # Utk mengambil depannya saja
print(f"Data = {data}")

data = data_2D[1][0]  
print(f"Data = {data}")

# Mengeluarkan Address semuanya
print("\n" + "=" * 3 + "Mengeluarkan Address semuanya" + "=" * 3)

print(f"Address data_2D (Asli)= {hex(id(data_2D))}")
print(f"Address data_2D_copy (Copy)= {hex(id(data_2D_copy))}")

print("Address dari member ke-1")
print(f"Address data_2D (Asli)= {hex(id(data_2D[0]))}")
print(f"Address data_2D_copy (Copy)= {hex(id(data_2D_copy[0]))}")

data_2D = [data_0,data_1, 10]
data_2D[1][0] = 5
data_2D[2] = 9

print(f"Data = {data_2D}")
print(f"Data Copy = {data_2D_copy}")

# Kita gunakan Deepcopy
print("\nKita gunakan Deepcopy")
from copy import deepcopy
data_2D = [data_0,data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Address data_2D (Asli)= {hex(id(data_2D))}")
print(f"Address data_2D_copy (Copy)= {hex(id(data_2D_deepcopy))}")

print("\nAddress dari member ke-1")
print(f"Address data_2D (Asli)= {hex(id(data_2D[0]))}")
print(f"Address data_2D_copy (Copy)= {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"Data = {data_2D}")
print(f"Data Copy = {data_2D_copy}")
print(f"Data Deep = {data_2D_deepcopy}")






































































































print("\n")