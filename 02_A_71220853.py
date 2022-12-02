kata = input (" Masukkan kata : ")
jumlah = int(len(kata))

def cetakHuruf(kata):
    if jumlah % 2 == 0 :
        x = kata[0:3]
        y = kata[-3:]
        print ("Huruf yang diambil pada kata ",kata,"adalah",x," dan",y)

    else :
        p = int((jumlah-3)/2)
        q = kata[p:-p]
        print ("Huruf yang diambil pada kata ", kata, "adalah ", q)

cetakHuruf(kata)
