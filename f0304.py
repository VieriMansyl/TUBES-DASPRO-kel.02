#ini dari algoritma utama
#gadget = []
#gadget = load("csv")
# F03

def carirarity(gadget) :

    rarity = input("Masukkan rarity: ")
    
    print("Hasil pencarian: \n")

    if (len(gadget)) == 0 :
        print("Tidak ditemukan gadget dengan rarity", rarity)
    else :
        for i in range(len(gadget)) :
            for j in range(len(gadget[i])) :
                if rarity == gadget[i][j][4] :
                    print("Nama             :", gadget[i][j][1])
                    print("Deskripsi        :", gadget[i][j][2])
                    print("Jumlah           :", gadget[i][j][3])
                    print("Rarity           :", gadget[i][j][4])
                    print("Tahun ditemukan  :", gadget[i][j][5], "\n")

# F04 

def caritahun(gadget) :

    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")    

    print("Hasil pencarian: \n")
    if (len(gadget)) == 0 :
        print("Tidak ditemukan gadget yang memenuhi tahun",kategori, tahun)
    else :
        if kategori == "=" :  
            for i in range(len(gadget)) :
                for j in range(1, len(gadget[i])) :
                    if tahun == int(gadget[i][j][5]) :
                        print("Nama             :", gadget[i][j][1])
                        print("Deskripsi        :", gadget[i][j][2])
                        print("Jumlah           :", gadget[i][j][3])
                        print("Rarity           :", gadget[i][j][4])
                        print("Tahun ditemukan  :", gadget[i][j][5], "\n")
        elif kategori == ">" :
            for i in range(len(gadget)) :
                for j in range(1, len(gadget[i])) :
                    if int(gadget[i][j][5]) > tahun :
                        print("Nama             :", gadget[i][j][1])
                        print("Deskripsi        :", gadget[i][j][2])
                        print("Jumlah           :", gadget[i][j][3])
                        print("Rarity           :", gadget[i][j][4])
                        print("Tahun ditemukan  :", gadget[i][j][5], "\n")
        elif kategori == "<" :
            for i in range(len(gadget)) :
                for j in range(1, len(gadget[i])) :
                    if int(gadget[i][j][5]) < tahun :
                        print("Nama             :", gadget[i][j][1])
                        print("Deskripsi        :", gadget[i][j][2])
                        print("Jumlah           :", gadget[i][j][3])
                        print("Rarity           :", gadget[i][j][4])
                        print("Tahun ditemukan  :", gadget[i][j][5], "\n")
        elif kategori == ">=" :
            for i in range(len(gadget)) :
                for j in range(1, len(gadget[i])) :
                    if int(gadget[i][j][5]) >= tahun :
                        print("Nama             :", gadget[i][j][1])
                        print("Deskripsi        :", gadget[i][j][2])
                        print("Jumlah           :", gadget[i][j][3])
                        print("Rarity           :", gadget[i][j][4])
                        print("Tahun ditemukan  :", gadget[i][j][5], "\n")
        elif kategori == "<=" :
            for i in range(len(gadget)) :
                for j in range(1, len(gadget[i])) :
                    if int(gadget[i][j][5]) <= tahun :
                        print("Nama             :", gadget[i][j][1])
                        print("Deskripsi        :", gadget[i][j][2])
                        print("Jumlah           :", gadget[i][j][3])
                        print("Rarity           :", gadget[i][j][4])
                        print("Tahun ditemukan  :", gadget[i][j][5], "\n")
