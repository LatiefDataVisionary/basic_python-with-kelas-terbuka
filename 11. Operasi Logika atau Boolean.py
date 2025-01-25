# Operasi Logika atau Boolean (Tabel Kebenaran)
# Not, Or, And, Xor
print("\n" + "=" * 10 + "Operasi Logika atau Boolean (Tabel Kebenaran)" + "=" * 10)
print("=" * 3 + "Not, Or, And, Xor" + "=" * 3 + "\n")

# NOT
print("====NOT===")
a = True
c = not a
print("Data a = ", a)
print("-----------NOT")
print("Data c = ", c)
print("\n")

a = False
c = not a
print("Data a = ", a)
print("-----------NOT")
print("Data c = ", c)
print("\n")


# OR (Jika salah satu TRUE, maka hasilnya adalah TRUE)
# Ini kayak 1 adalah TRUE, dan 0 adalah FALSE dlm PENJUMLAHAN
""""
     Maka;
     0 + 0 = 0  (FALSE)
     0 + 1 = 1  (TRUE)
     1 + 0 = 1  (TRUE)
     1 + 1 = 2  (TRUE)
"""
print("====OR===")
a = False
b = False
c = a or b
print(a, " OR ", b, " = ", c)

print("====OR===")
a = False
b = True
c = a or b
print(a, " OR ", b, " = ", c)

print("====OR===")
a = True
b = False
c = a or b
print(a, " OR ", b, " = ", c)

print("====OR===")
a = True
b = True
c = a or b
print(a, " OR ", b, " = ", c)

print("\n")


# AND (Jika dua buah nilai TRUE, maka hasil TRUE)
# Ini kayak 1 adalah TRUE, dan 0 adalah FALSE dlm PERKALIAN
""""
     Maka;
     0 * 0 = 0  (FALSE)
     0 * 1 = 1  (FALSE)
     1 * 0 = 0  (FALSE)
     1 * 1 = 2  (TRUE)
"""

print("====AND===")
a = False
b = False
c = a and b
print(a, " AND ", b, " = ", c)

print("====AND===")
a = False
b = True
c = a and b
print(a, " AND ", b, " = ", c)

print("====AND===")
a = True
b = False
c = a and b
print(a, " AND ", b, " = ", c)

print("====AND===")
a = True
b = True
c = a and b
print(a, " AND ", b, " = ", c)

# XOR (Akan TRUE jika salah satu TRUE, sisanya FALSE)
print("====XOR===")
a = False
b = False
c = a ^ b
print(a, " XOR ", b, " = ", c)

print("====XOR===")
a = False
b = True
c = a ^ b
print(a, " XOR ", b, " = ", c)

print("====XOR===")
a = True
b = False
c = a ^ b
print(a, " XOR ", b, " = ", c)

print("====XOR===")
a = True
b = True
c = a ^ b
print(a, " XOR ", b, " = ", c)


print("\n")





























































































































