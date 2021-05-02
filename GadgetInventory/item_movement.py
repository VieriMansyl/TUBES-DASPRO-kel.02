#Contributor : Vieri Mansyl - 16520056

#FUNCTION

#dic_to_li_buku_hutang      : changes dictionaries into list of list
#parameter                  : buku_hutang_dic
#return value               : buku_hutang_li

#li_to_dic_buku_hutang      : changes list of list into dictionaries 
#parameter                  : buku_hutang_li
#return value               : buku_hutang_dic

#isKabisat                  : check a leap year
#parameter                  : year
#return value               : TRUE / FALSE

#isDateValid                : check whether a date is valid
#parameter                  : d  (date) , m (month) , y (year)
#return value               : TRUE / FALSE

#validasi_tanggal           : validate every date component 9such as the date, month , and year)
#parameter                  : tanggal
#return value               : TRUE / FALSE

#validasi_pinjamgadget      : validate each attributes of 'borrow gadget(s)' module - F08
#parameter                  : datas_gadget_id , datas_gadget_jumlah
#return value               : cek_id , tanggal_pinjam , jumlah_pinjam , index_id

#validasi_balikgadget       : validate each attributes of 'return gadget(s)' module - F09
#parameter                  : pinjaman_user
#return value               : nomor_return , tanggal_return , jumlah_return , index_id

#validasi_mintaconsumable  : validate each attributes of 'request consumable(s)' module - F10
#parameter                  : datas_consume_id , datas_consume_jumlah
#return value               : cek_id , jumlah_consume , tanggal_consume , index_id


#pinjam                     : borrow gadget <execute module F08>
#parameter                  : user_name , identity , datas_gadget , buku_hutang_li , gadget_borrow_history
#return value               : datas_gadget , buku_hutang_li , gadget_borrow_history

#kembalikan                 : return gadget <execute module F09>
#parameter                  : user_name , user_identity , datas_gadget , buku_hutang_li , gadget_borrow_history , gadget_return_history
#return value               : datas_gadget , buku_hutang_li , gadget_return_history

#minta                      : demand consumable <execute module F10>
#parameter                  : user_name , datas_consume , history_minta
#return value               : datas_consume , history_minta


def dic_to_li_buku_hutang(buku_hutang_dic):
    new_datas = []
    new_1 = [nama for nama in buku_hutang_dic["nama"]]
    new_2 = [jumlah for jumlah in buku_hutang_dic["nama_gadget"]]
    new_3 = [jumlah for jumlah in buku_hutang_dic["jumlah"]]

    for i in range(len(buku_hutang_dic["nama"])):
        new_datas.append( [new_1[i] , new_2[i]] , new_3[i] )
    return new_datas

def li_to_dic_buku_hutang(buku_hutang_li):
    buku_hutang_dic = {"nama" : [] , "nama_gadget": [] , "jumlah" : []}
    buku_hutang_dic["nama"] = [data[0] for data in buku_hutang_li]
    buku_hutang_dic["nama_gadget"] = [data[1] for data in buku_hutang_li]
    buku_hutang_dic["jumlah"] = [int(data[2]) for data in buku_hutang_li]
    return buku_hutang_dic


def isKabisat(year):
    if ((year % 4) == 0 and (year % 100) != 0) or ((year % 400) == 0):
        return True
    else:
        return False

def isDateValid (d,m,y):
    if (y >= 0):
        if (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12) and (d >= 1 and d <= 31) :
            return True
        elif ((m == 4) or (m == 6) or (m == 9) or (m == 11)) and (d >= 1 and d <= 30) :
            return True
        elif  (m == 2) and isKabisat(y) and (d >= 1 and d <= 29) :
            return True
        elif  (m == 2) and (not isKabisat(y)) and (d >= 1 and d <= 28) :
            return True
        else:
            return False
    else:
        return False

def validasi_tanggal(tanggal):
    if len(tanggal) < 10:
        return False
    else:
        validate = tanggal.split("/")
        try:
            cek_date = int(validate[0])
        except ValueError:
            return False
        try:
            cek_month = int(validate[1])
        except ValueError:
            return False
        try:
            cek_year = int(validate[2])
        except ValueError:
            return False
        
    return isDateValid(cek_date , cek_month , cek_year)



def validasi_pinjamgadget(datas_gadget_id , datas_gadget_jumlah):                                               #validasi value tiap atribut peminjaman gadget
    cek = 0
    while cek < 2:
        cek = 0
        cek_id = input('Masukan ID item: ').upper()
        tanggal_pinjam = input('Tanggal peminjaman (DD/MM/YYYY): ')
        if not validasi_tanggal(tanggal_pinjam) :
            print("Masukan tanggal salah, silahkan coba lagi")
            continue
        try :
            jumlah_pinjam = int(input("Jumlah peminjaman: "))
        except ValueError:
            print("Masukan salah, silahkan coba lagi")
            continue

        if cek_id not in datas_gadget_id:
            print('Id tidak ada, silahkan coba lagi')
        else:
            index_id = datas_gadget_id.index(cek_id)
            cek += 1
            if jumlah_pinjam <= 0:
                print('Masukan tidak diterima , silahkan coba lagi')
            elif datas_gadget_jumlah[index_id] == 0:
                print('Stok barang telah habis, silahkan meminjam gadget lain')
            elif jumlah_pinjam > int(datas_gadget_jumlah[index_id]):
                print('Jumlah yg diinginkan berlebihan, stok tidak cukup! Silahkan coba lagi')
            else:
                cek += 1

    return tanggal_pinjam , jumlah_pinjam , index_id

def validasi_balikgadget(pinjaman_user):                                                                        #validasi value tiap atribut pengembalian gadget
    cek = 0
    while cek < 2:
        cek = 0
        try :
            nomor_return = int(input("Masukan nomor peminjaman: "))
        except ValueError:
            print("Masukan nomor salah, silahkan coba lagi")
            continue

        tanggal_return = input("Tanggal pengembalian (DD/MM/YYYY): ")
        if not validasi_tanggal(tanggal_return) :
            print("Masukan tanggal salah, silahkan coba lagi")
            continue

        try :
            jumlah_return = int(input("Jumlah yang ingin dibalikkan: "))
        except ValueError:
            print("Masukan jumlah salah, silahkan coba lagi")
            continue

        if nomor_return > len(pinjaman_user['nama_gadget']) :
            print('Nomor tidak ada , silahkan coba lagi')
        else:
            index_id = nomor_return-1
            cek += 1
            if jumlah_return <= 0:
                print('Masukan tidak diterima , silahkan coba lagi')
            elif jumlah_return > int(pinjaman_user['jumlah_pinjaman'][index_id]):
                print('jumlah yang ingin dikembalikan berlebihan, silahkan coba lagi')
            else:
                cek += 1
    return tanggal_return , jumlah_return , index_id

def validasi_mintaconsumable(datas_consume_id , datas_consume_jumlah):                                          #validasi value tiap atribut consumable
    cek = 0
    while cek < 2:
        cek = 0

        cek_id = input('Masukan ID item: ').upper()

        try :
            jumlah_consume = int(input('Jumlah: '))
        except ValueError:
            print("Masukan salah, silahkan coba lagi")
            continue

        tanggal_consume = input("Tanggal permintaan (DD/MM/YYYY): ")
        if not validasi_tanggal(tanggal_consume) :
            print("Masukan tanggal salah, silahkan coba lagi")
            continue

        if cek_id not in datas_consume_id:
            print('Id tidak ada , silahkan coba lagi')
        else:
            index_id = datas_consume_id.index(cek_id)
            cek += 1
            if jumlah_consume <= 0:
                print('masukan tidak diterima , silahkan coba lagi')
            elif datas_consume_jumlah[index_id] == 0:
                print('Stok barang telah habis, silahkan meminjam gadget lain')
            elif jumlah_consume > datas_consume_jumlah[index_id]:
                print('Jumlah yg diinginkan berlebihan, stok tidak cukup! Silahkan coba lagi')
            else:
                cek += 1
    return jumlah_consume , tanggal_consume , index_id



def pinjam(user_name , identity , datas_gadget , buku_hutang_li , gadget_borrow_history):
    #list datas secondary (gadget) -> untuk mengecek keberadaan item gadget
    datas_gadget_id     = [data[0] for data in datas_gadget]
    datas_gadget_jumlah = [data[3] for data in datas_gadget]

    #VALIDASI DATA
    tanggal_pinjam, jumlah_pinjam, index_id = validasi_pinjamgadget(datas_gadget_id , datas_gadget_jumlah)

    #gadget dipinjam dari datas_gadget dan tercatat ke buku_hutang_dic
    buku_hutang_dic = li_to_dic_buku_hutang(buku_hutang_li)                                          #konversi buku hutang dari list of list ke dictionaries

    #cek nama user dan nama gadget dalam buku_hutang_dic
    data_nama  = [data[0]]

    datas_hutang_nama   = buku_hutang_dic["nama"][:]
    datas_hutang_gadget = buku_hutang_dic["nama_gadget"][:]
    exist = False
    for i in range(len(datas_hutang_nama)):
        if (user_name == datas_hutang_nama[i]) and (datas_gadget[index_id][1] == datas_hutang_gadget[i]):
                print(f"Gadget {datas_gadget[index_id][1]} belum dikembalikan seluruhnya. Mohon segera mengembalikannya.")
                exist = True
    
    if not exist:
        buku_hutang_dic['nama'].append(user_name)
        buku_hutang_dic["nama_gadget"].append(datas_gadget[index_id][1])
        buku_hutang_dic['jumlah'].append(jumlah_pinjam)

        print(f"Item {datas_gadget[index_id][1]} (x{jumlah_pinjam}) berhasil dipinjam!")
        datas_gadget[index_id][3] -= jumlah_pinjam

    buku_hutang_li = dic_to_li_buku_hutang(buku_hutang_dic)                                          #konversi buku hutang dari dictionaries ke list of list

    #gadget tercatat ke gadget_borrow_history
    ID_pinjam = len(gadget_borrow_history) + 1
    data_history = [ID_pinjam , identity , datas_gadget[index_id][0] , tanggal_pinjam , jumlah_pinjam]
    gadget_borrow_history.append(data_history)

    return datas_gadget , buku_hutang_li , gadget_borrow_history

def kembalikan(user_name , user_identity , datas_gadget , buku_hutang_li , gadget_borrow_history , gadget_return_history):
    #list datas secondary (gadget) -> untuk mengecek keberadaan item gadget
    datas_gadget_name   = [data[1] for data in datas_gadget]

    buku_hutang_dic     = li_to_dic_buku_hutang(buku_hutang_li)                                     #konversi buku hutang dari dictionaries ke list of list

    #kasus apabila belum terjadi peminjaman gadget
    datas_hutang_nama   = buku_hutang_dic["nama"][:]
    datas_hutang_gadget = buku_hutang_dic["nama_gadget"][:]
    exist = False

    #list gadget yang dipinjam oleh user
    pinjaman_user = {"nama_gadget":[] , "jumlah_pinjaman" : []}                                     #rekapan gadget dan jumlah pinjaman dari seorang user

    for i in range(len(datas_hutang_nama)):                                                         #cek ada_tidaknya gadget yang masih dipinjam oleh user
        if user_name == datas_hutang_nama[i]:
                exist = True
    
    if exist:
        for i in range(len(datas_hutang_nama)):
            if user_name == datas_hutang_nama[i]:
                    print(f"{i+1}. {datas_hutang_gadget[i]} (x{buku_hutang_dic['jumlah'][i]})")
                    
                    #merekap gadget pinjaman serta jumlah pinjamannya dari user
                    pinjaman_user["nama_gadget"].append(datas_hutang_gadget[i])
                    pinjaman_user["jumlah_pinjaman"].append(buku_hutang_dic['jumlah'][i])
    else:
        print("Belum ada peminjaman")
        buku_hutang_li = dic_to_li_buku_hutang(buku_hutang_dic)                                      #konversi buku hutang dari dictionaries ke list of list
        return datas_gadget , buku_hutang_li , gadget_return_history


    #VALIDASI DATA
    tanggal_return, jumlah_return, index_id = validasi_balikgadget(pinjaman_user)

    gadget_kembalian = pinjaman_user['nama_gadget'][index_id]
    print(f"Item {gadget_kembalian} (x{jumlah_return}) telah dikembalikan!")

    for i in range(len(datas_hutang_nama)):
        if (user_name == buku_hutang_dic['nama'][i]) and (gadget_kembalian == buku_hutang_dic['nama_gadget'][i]):
            indeks_gadget_pinjaman = i

    #gadget keluar dari buku_hutang_dic
    buku_hutang_dic['jumlah'][indeks_gadget_pinjaman] = int(buku_hutang_dic['jumlah'][indeks_gadget_pinjaman]) - jumlah_return

    #gadget kembali ke datas_gadget
    index_barang            = datas_gadget_name.index(gadget_kembalian)                            #letak indeks gadget hasil pinjaman pada list gadget
    datas_gadget[index_barang][3] += jumlah_return                                                 #stok gadget bertambah setelah dikembalikan

    #gadget tercatat ke gadget_return_history
    ID_kembalian        = len(gadget_return_history) + 1
    id_gadget           = datas_gadget[index_barang][0]
    indeks_ID_pinjam    = 0

    for i in range(len(gadget_borrow_history)):
        if user_identity == gadget_borrow_history[i][1] and id_gadget == gadget_borrow_history[i][2]:
            indeks_ID_pinjam = i

    data_history        = [ID_kembalian , gadget_borrow_history[indeks_ID_pinjam][0] , tanggal_return , jumlah_return]
    gadget_return_history.append(data_history)

    #kondisi ketika gadget telah dikembalikan semuanya
    if buku_hutang_dic['jumlah'][indeks_gadget_pinjaman] == 0 :
        print(f"Selamat! Item {gadget_kembalian} telah dikembalikan semua!")
        buku_hutang_dic['nama'].remove(buku_hutang_dic['nama'][indeks_gadget_pinjaman])                 #menghapus nama user dengan value kosong
        buku_hutang_dic['nama_gadget'].remove(buku_hutang_dic['nama_gadget'][indeks_gadget_pinjaman])   #menghapus nama gadget dengan value kosong
        buku_hutang_dic['jumlah'].remove(0)                                                             #menghapus jumlah gadget bernilai 0

    buku_hutang_li = dic_to_li_buku_hutang(buku_hutang_dic)                                             #konversi buku hutang dari dictionaries ke list of list

    return datas_gadget , buku_hutang_li , gadget_return_history

def minta(user_identity , datas_consume , history_minta):
    #list datas secondary (consumable)
    datas_consume_id = [data[0] for data in datas_consume]
    datas_consume_jumlah = [data[3] for data in datas_consume]

    jumlah_consume, tanggal_consume, index_id = validasi_mintaconsumable(datas_consume_id , datas_consume_jumlah)        #VALIDASI DATA

    print(f"Item {datas_consume[index_id][1]} (x{jumlah_consume}) telah berhasil diambil!")
    datas_consume[index_id][3] -= jumlah_consume                                                                         #consumable terambil dari stok consumable

    #consumable tercatat ke history_minta
    ID_minta  = len(history_minta) + 1
    new_datas = [ID_minta , user_identity , datas_consume[index_id][0] , tanggal_consume , jumlah_consume]
    history_minta.append(new_datas)

    return datas_consume , history_minta

