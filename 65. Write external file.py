# 1. Mode write

# dia akan membuat file baru jika tdk ada
# lalu akan menimpa atau overwrite isinya

with open("65_data_1.txt","w",encoding="utf-8") as file:
    file.write("Ucup surucup")
    
with open("65_data_1.txt","w",encoding="utf-8") as file:
    file.write("Jon si Joni")

with open("65_data_1.txt","w",encoding="utf-8") as file:
    file.write("overwrite")


# 2. Mode append 

with open("65_data_2.txt","w",encoding="utf-8") as file:
    file.write("Jon si Joni\n")

with open("65_data_2.txt","a",encoding="utf-8") as file:
    file.write("Ucup surucup\n")

with open("65_data_2.txt","a",encoding="utf-8") as file:
    file.write("tambah lagi dg append(a)\n")



# 3. Mode r+

with open("65_data_3.txt","w",encoding="utf-8") as file:
    file.write("Data ke 3\n")

with open("65_data_3.txt","r+",encoding="utf-8") as file:
    file.write("baris 1\n")
    file.write("baris 2\n")
    file.write("baris 3\n")

with open("65_data_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("65_data_3.txt","r+",encoding="utf-8") as file:
    file.write("otong")  # menimpa isi text sesuai dg panjang data
















































