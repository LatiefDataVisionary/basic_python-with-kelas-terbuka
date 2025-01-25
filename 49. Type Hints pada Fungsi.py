### TYPE HINTS PADA FUNGSI
print("\n" + "=" * 10 + "TYPE HINTS PADA FUNGSI" + "=" * 10 + "\n")

## Bentuk standar Fungsi yg telah kita pelajari

'''
Studi Kasus
def fungsi(parameter):
    hasil = parameter ** 2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

def sepuluh_pangkat(parameter:int) -> int:
    '''Fungsi dg Hints'''
    output = 10 ** parameter
    return output
 
HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:str):
    print(argument)

display("Ucup")

import os

hasil = os.system("cls")
print(hasil)








































































































print("\n")