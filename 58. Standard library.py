import datetime

print()
data_waktu = datetime.datetime.now()
print(f"Datetime now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime("%A")}")


from collections import Counter
data_huruf = ["a","b","c","d","a","d","a"]

hitung_a = 0 
for i in data_huruf:
    if i == "a":
        hitung_a += 1
        
print(f"\nJumlah huruf a: {hitung_a}")


hitung_b = 0 
for i in data_huruf:
    if i == "b":
        hitung_b += 1
        
print(f"Jumlah huruf b: {hitung_b}\n")


data_count = Counter(data_huruf)
print(f"Data Count = {data_count}")
print(f"Jumlah a = {data_count['a']}")
print(f"Jumlah d = {data_count['d']}")


## Buat open file
import io 

file = io.open("file_text.txt", "r")
print()
print(file.read())












print()