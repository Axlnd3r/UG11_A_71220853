

def ubahKata():
    e = input (" Masukkan sebuah kalimat/kata : ")
    f = input (" Masukkan kata yang ingin diubah :")
    g = input (" Masukkan kata pengganti : ")
    h = e.replace(f,g)
    return h

def hitungKata ():
    j = e.count (y)
    return j

print ("====== Program Manipulasi String ======")
a = print (" Pilihan Menu :")
b= print (" 1. Hitung kata ")
c= print (" 2. Ubah kata")

d = int(input(" Pilihan anda : "))


if d == 1:
    e = input (" Masukkan sebuah kalimat/kata : ")
    y = input (" Masukkan kata yang ingin dihitung :")
    print (" Terdapat sebanyak", hitungKata (), "kata", y, "didalam kalimat")
    
elif d == 2:
    berubah = ubahKata ()
    print ("String berhasil diubah menjadi :", berubah)

else :
    print ( " Tidak ada pilihan ")
