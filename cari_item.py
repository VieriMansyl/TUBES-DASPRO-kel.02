#F03
def carirarity(gadget) :
    #menerima input berupa rarity
    rarity = input("Masukkan rarity: ")
    #mengeluarkan output
    print("Hasil pencarian: \n")
    #inisiasi jumlah data
    jumlahdata = 0

    if (len(gadget)) == 0 : #ketika data kosong
        print("Tidak ditemukan gadget dengan rarity", rarity)
    else : #data ada
        #looping untuk mengecek seluruh data untuk print data
        for i in range(1, len(gadget)) :
            if rarity == gadget[i][4] :
                print("Nama             :", gadget[i][1])
                print("Deskripsi        :", gadget[i][2])
                print("Jumlah           :", gadget[i][3])
                print("Rarity           :", gadget[i][4])
                print("Tahun ditemukan  :", gadget[i][5], "\n")
        #looping untuk mengecek jumlah data yang cocok
        for i in range(1,len(gadget)) :
            if rarity == gadget[i][4] :
                jumlahdata += 1
            else :
                jumlahdata += 0
        #ketika jumlah data = 0, output berbeda
        if jumlahdata == 0 :
            print("Tidak ada gadget yang ditemukan")

# F04 
def caritahun(gadget) :
    #menerima input berupa tahun dan kategori
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ") 
    #inisiasi jumlah data
    jumlahdata = 0   
    #mengeluarkan output
    print("Hasil pencarian: \n")

    if (len(gadget)) == 0 : #ketika data kosong
        print("Tidak ada gadget yang ditemukan")
    else : #data ada
        if kategori == "=" :  
            #looping untuk mengecek seluruh data untuk print data
            for i in range(1, len(gadget)) :
                if tahun == int(gadget[i][5]) :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
            #looping untuk mengecek jumlah data yang cocok
            for i in range(1,len(gadget)) :
                if tahun == int(gadget[i][5]) :
                    jumlahdata += 1
                else :
                    jumlahdata += 0
            #ketika jumlah data = 0, output berbeda
            if jumlahdata == 0 :
                print("Tidak ada gadget yang ditemukan")

        elif kategori == ">" :
            #looping untuk mengecek seluruh data untuk print data
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) > tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
            #looping untuk mengecek jumlah data yang cocok
            for i in range(1,len(gadget)) :
                if int(gadget[i][5]) > tahun :
                    jumlahdata += 1
                else :
                    jumlahdata += 0
            #ketika jumlah data = 0, output berbeda
            if jumlahdata == 0 :
                print("Tidak ada gadget yang ditemukan")

        elif kategori == "<" :
            #looping untuk mengecek seluruh data untuk print data
    
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) < tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
            #looping untuk mengecek jumlah data yang cocok
            for i in range(1,len(gadget)) :
                if int(gadget[i][5]) < tahun :
                    jumlahdata += 1
                else :
                    jumlahdata += 0
            #ketika jumlah data = 0, output berbeda
            if jumlahdata == 0 :
                print("Tidak ada gadget yang ditemukan")
    
        elif kategori == ">=" :
            #looping untuk mengecek seluruh data untuk print data
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) >= tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
            #looping untuk mengecek jumlah data yang cocok
            for i in range(1,len(gadget)) :
                if int(gadget[i][5]) >= tahun :
                    jumlahdata += 1
                else :
                    jumlahdata += 0
            #ketika jumlah data = 0, output berbeda
            if jumlahdata == 0 :
                print("Tidak ada gadget yang ditemukan")

        elif kategori == "<=" :
            #looping untuk mengecek seluruh data untuk print data
            for i in range(1, len(gadget)) :
                if int(gadget[i][5]) <= tahun :
                    print("Nama             :", gadget[i][1])
                    print("Deskripsi        :", gadget[i][2])
                    print("Jumlah           :", gadget[i][3])
                    print("Rarity           :", gadget[i][4])
                    print("Tahun ditemukan  :", gadget[i][5], "\n")
            #looping untuk mengecek jumlah data yang cocok
            for i in range(1,len(gadget)) :
                if int(gadget[i][5]) <= tahun :
                    jumlahdata += 1
                else :
                    jumlahdata += 0
            #ketika jumlah data = 0, output berbeda
            if jumlahdata == 0 :
                print("Tidak ada gadget yang ditemukan")
