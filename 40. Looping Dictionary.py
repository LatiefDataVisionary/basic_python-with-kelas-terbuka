## LOOPING DICTIONARY
print('\n' + '=' * 10 + "LOOPING DICTIONARY" + '=' * 10 + '\n')

teman_teman = {
    "cup":"Ucup Surucup",
    "tong":"Otong Surotong",
    "dung":"Dudung Surudung",
    "sep":"Asep si Kasyep",
    "cuy":"Ucuy Surucuy"
}

# Looping First Try (yg keluar adalah Key nya)
print("---Looping First Try---")

for teman in teman_teman:
    print(teman)

# Operator utk mengambil Item/Iterables
print("\n---Looping First Try---")
keys = teman_teman.keys()
print(keys)
print("\n")

for key in teman_teman.keys():
    print(key)

print("\n")
for key in teman_teman.keys():
    print(teman_teman.get(key))

print("\n")
values = teman_teman.values()  # utk mengambil value nya saja
print(values)

print("\n")
for value in teman_teman.values():
    print(value)

print("\n")
items = teman_teman.items()
print(items)

print("\n")
for item in teman_teman.items():  # Keluarannya Tupple
    print(item)

print("\n")
for key,value in teman_teman.items():
    print(f"Key = {key}, Value = {value}")

























































































print("\n")