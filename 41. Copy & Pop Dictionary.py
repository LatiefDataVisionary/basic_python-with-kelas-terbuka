## COPY & POP DICTIONARY
print("\n" + "=" * 10 + "COPY & POP DICTIONARY" + "=" * 10 + "\n")

teman_teman = {
    "cup":"Ucup Surucup",
    "tong":"Otong Surotong",
    "dung":"Dudung Surudung",
    "sep":"Asep si Kasyep",
    "cuy":"Ucuy Surucuy",
}

friends = teman_teman

print(f"Teman-teman: {teman_teman}\n")
print(f"Friends: {friends}\n")

teman_teman["cup"]="Ucup si Kweren"
print(f"Teman-teman: {teman_teman}\n")
print(f"Friends: {friends}\n")

friends = teman_teman.copy() 
# jika value disuatu key di teman_teman di ganti
# maka value di key di friends tdk berubah

print(f"Teman-teman: {teman_teman}\n")
print(f"Friends: {friends}\n")

teman_teman["cup"]="Ucup si Kweren"
print(f"Teman-teman: {teman_teman}\n")
print(f"Friends: {friends}\n")


## Pop Dictionary (mengambil data berdasarkan Key)
print("\n===Pop Dictionary==")

dataAsep = friends.pop("sep")
print(f"Data Asep = {dataAsep}\n")
print(f"Friends = {friends}")
# key dan value di sep hilang karena di pop
# krn ditransfer dari friends ---> dataAsep


## Popitem Dictionary (mengambil data Key terakhir)
print("\n===Popitem Dictionary===")

dataTerakhir = friends.popitem()
print(f"Data Terakhir = {dataTerakhir}\n")
print(f"Friends = {friends}")





























































































print("\n")