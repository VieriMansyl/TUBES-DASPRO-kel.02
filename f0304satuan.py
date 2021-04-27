#gadget = nama list dari gadget.csv

#databases = load("csv")
#ini databases[0] tapi bisa aja databases[1] ato databases[2] jadi harus liat lagi
#gadget = databases[0]
#print(gadget)


#F03
def carirarity(gadget) :

    rarity = input("Masukkan rarity: ")
    
    print("Hasil pencarian: \n")

    if (len(gadget)) == 0 :
        print("Tidak ditemukan gadget dengan rarity", rarity)
    else :
        for i in range(1, len(gadget)) :
            if rarity == gadget[i][4] :
                print("Nama             :", gadget[i][1])
                print("Deskripsi        :", gadget[i][2])
                print("Jumlah           :", gadget[i][3])
                print("Rarity           :", gadget[i][4])
                print("Tahun ditemukan  :", gadget[i][5], "\n")

# F04 

def caritahun(gadget) :

    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")    

    print("Hasil pencarian: \n")
    if (len(gadget)) == 0 :
        print("Tidak ditemukan gadget yang memenuhi tahun",kategori, tahun)
    else :
        if kategori == "=" :  
            for i in range(1, len(gadget)) :
                if tahun == int(gadget[i][5]) :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == ">" :
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) > tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == "<" :
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) < tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == ">=" :
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) >= tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == "<=" :
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) <= tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
