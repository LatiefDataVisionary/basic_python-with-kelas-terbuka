data = "Ini adalah String"
print(data)
print(type(data))

# 1. Cara membuat String 

"""
    1. Menggunakan single quote '.....'
    2. Menggunakan douvle quote "....."
"""

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari Jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print("Mari shalat Jum\'at")
print('G\'day, isn\'t it?')

# Backslash
print("C:\\user\\Ucup")

# Tab
print("Ucup\totong, semakin jauhan")

# Backspace 
print("Ucup \botong, jadi deketan")

# Newline
print("Baris pertama, \nbaris kedua.")  # LF --> Line Feed --> Unix, MacOs, Linux
print("Baris pertama, \rBaris kedua")   # CR --> Carriage Return --> Commodore, Acorn, Lisp
print("Baris pertama, \r\nbaris kedua")  # CRLF --> Line Feed Carriage Return --> Dipakai oleh Windows

# 3. String Literal atau Raw 

# Hati hati 
print("C:\\new folder") # Akan salah pathnya

# Menggunakan Raw String
print(r"C:\new folder")

# Multiline Literal String
print("""
Nama : Ucup
Kelas : 3 SD
      """)

# Multiline Literal String dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD|new Normal
Website : www.ucup.com/newID
""")























































































