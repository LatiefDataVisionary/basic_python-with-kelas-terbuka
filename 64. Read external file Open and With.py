## Tutorial membaca file eksternal

print("\n","="*3,"Membaca File Txt","="*3,"\n")
file =open("data64.txt",mode="r")

print(f"Status read : {file.readable()}")
print(f"Status write : {file.writable()}")

## Baca sluruh file 
print(file.read())


# ## baca per baris
# print(file.readline(), end="")  # baca baris pertama
# print(file.readline(), end="")  # baca baris kedua


# ## Baca semua baris
# print(file.readlines())

print(f"Apakah file sudah di close : {file.closed}")
file.close()
print(f"Apakah file sudah di close : {file.closed}")



## salah satu teknik membuka file di python 

print("\n","="*3,"Membaca File Txt dg with","="*3,"\n")

with open("data64.txt", mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"Apakah file sudah di close : {file.closed}")
    
    if file.closed == True:
        bukaTutup = "Sudah"        
    else:
        bukaTutup = "Belum"
    print(f"Lagi ya!! Apakah file sudah di close : {bukaTutup}")


print()
# bukaTutup = ""
if file.closed == True:
    bukaTutup = "Sudah"        
else:
    bukaTutup = "Belum"
print(f"Apakah file sudah di close : {bukaTutup}\n")









