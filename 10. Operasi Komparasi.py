# Operasi Komparasi 
print("\n" + "=" * 10 + "Operasi Komparasi" + 10 * "=" + "\n")
# Setiap hasil dari Operasi Komparasi adalah BOOLEAN 

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari > 
print("\n=====Lebih Besar Dari (>)")
hasil = a > 3 
print(a,">",3,"=",hasil)
hasil = b > 3 
print(b,">",3,"=",hasil)
hasil = b > 2 
print(b,">",2,"=",hasil)

# Kurang Dari <
print("\n=====Kurang Dari (<)")
hasil = a < 3 
print(a,"<",3,"=",hasil)
hasil = b < 3 
print(b,"<",3,"=",hasil)
hasil = b < 2 
print(b,"<",2,"=",hasil)

# Lebih Dari Sama Dengan >=
print("\n=====Lebih Dari Sama Dengan (>=)")
hasil = a >= 3 
print(a,"",3,"=",hasil)
hasil = b >= 3 
print(b,">=",3,"=",hasil)
hasil = b >= 2 
print(b,">=",2,"=",hasil)

# Kurang Dari Sama Dengan <=
print("\n=====Kurang Dari Sama Dengan (<=)")
hasil = a <= 3 
print(a,"",3,"=",hasil)
hasil = b <= 3 
print(b,"<=",3,"=",hasil)
hasil = b <= 2 
print(b,"<=",2,"=",hasil)

# Sama Dengan (==)
print("\n=====Sama Dengan(==)")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak Sama Dengan (!=)
print("\n====Tidak Sama Dengan(!=)")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)


# 'Is' sebagai Komparasi Object Identity
print('\n\n=====Object Identity (is)')
x = 5 # Ini adalah Assignment membuat object 
y = 5
print("Nilai x = ",x,",ID = ",hex(id(x)))
print("Nilai y = ",y,",ID = ",hex(id(y)))
hasil = x is y 
print("x is y = ", hasil)

print('\n=====Object Identity (is )')
x = 5 # Ini adalah Assignment membuat object 
y = 6
print("Nilai x = ",x,",ID = ",hex(id(x)))
print("Nilai y = ",y,",ID = ",hex(id(y)))
hasil = x is y 
print("x is y = ", hasil)


# 'is not' sebagai Komparasi Object Identity
print('\n=====Object Identity (is not)')
x = 5 # Ini adalah Assignment membuat object 
y = 5
print("Nilai x = ",x,",ID = ",hex(id(x)))
print("Nilai y = ",y,",ID = ",hex(id(y)))
hasil = x is not y 
print("x is not y = ", hasil)

print('\n=====Object Identity (is not)')
x = 5 # Ini adalah Assignment membuat object 
y = 6
print("Nilai x = ",x,",ID = ",hex(id(x)))
print("Nilai y = ",y,",ID = ",hex(id(y)))
hasil = x is not y 
print("x is not y = ", hasil)






print("\n\n\n")
