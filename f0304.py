#gadget = nama list dari gadget.csv
# F03

def carirarity() :
    rarity = input("Masukkan rarity: \n")
    
    print("Hasil pencarian: \n")

    if (len(gadget)) == 0 :
        print("Tidak ditemukan gadget dengan rarity", rarity)
    else :
        for i in range(len(gadget)) :
            if rarity == gadget[i][4] :
                print("Nama             :", gadget[i][1])
                print("Deskripsi        :", gadget[i][2])
                print("Jumlah           :", gadget[i][3])
                print("Rarity           :", gadget[i][4])
                print("Tahun ditemukan  :", gadget[i][5], "\n")

# F04 

def caritahun() :
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: \n")    

    print("Hasil pencarian: \n")
    if (len(gadget)) == 0 :
        print("Tidak ditemukan gadget yang memenuhi tahun",kategori, tahun)
    else :
        if kategori == "=" :  
            for i in range(len(gadget)) :
                if tahun == gadget[i][5] :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == ">" :
            for i in range(len(gadget)) :
                if gadget[i][5] > tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == "<" :
            for i in range(len(gadget)) :
                if gadget[i][5] < tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == ">=" :
            for i in range(len(gadget)) :
                if gadget[i][5] >= tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
        elif kategori == "<=" :
            for i in range(len(gadget)) :
                if gadget[i][5] <= tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")

