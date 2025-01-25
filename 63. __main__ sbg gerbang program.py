## __main__ (dunder/double underscore) 
# adalah top level code enviroment

""" int main:{
    
}"""

# __name_ == "__main__" ini akan terjadi jika ada di file program utama 

## __name__ pd file program utama 
print(f"Nilai __name__ pada main.py = '{__name__}'")

## __name__ pd file program eksternal
import fungsi63

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"\nHasil tambah : {hasil}")

































































































