print("======= Program Manipulasi String ======")
menu = input("pilihan menu:")
b = print("1. hitungan kata")
c = print("2. ubah kata")

pilihan = int(input("pilihan anda:"))
 
def UbahKata():
    kalimat = input("masukan sebuah kalimat/kata: ")
    ubah    = input("masukan kata ynag ingin di ubah: ")
    penganti= input("masukan kata penganti: ")

    d = kalimat.replace (ubah,penganti)
    return d
e = UbahKata()
print("string berhasil di ubah menjadi:",e)

def hitungkata():
    kalimat = input("masukan kalimat/kata: ")
    hitung = input("masukan kata yang ingin di hitung: ")



