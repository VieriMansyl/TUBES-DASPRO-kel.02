#Contributor : Vieri Mansyl - 16520056

#Function
#validasi_pinjamgadget      : validate each attributes of 'borrow gadget(s)' module - F08
#parameter                  : datas_gadget_id , datas_gadget_jumlah
#return value               : cek_id , tanggal_pinjam , jumlah_pinjam , index_id

#validasi_balikgadget       : validate each attributes of 'return gadget(s)' module - F09
#parameter                  : datas_gadget_pinjam
#return value               : nomor_return , tanggal_return , jumlah_return , index_id

#validasi_mintaconsumable  : validate each attributes of 'request consumable(s)' module - F10
#parameter                  : datas_consume_id , datas_consume_jumlah
#return value               : cek_id , jumlah_consume , tanggal_consume , index_id

#pinjam                     : borrow gadget <execute module F08>
#parameter                  : user_name , datas_gadget , datas_gadget_pinjam , history_pinjam , ID_pinjam
#return value               : datas_gadget , datas_gadget_pinjam , history_pinjam , ID_pinjam , pernah_pinjam

#kembalikan                 : return gadget <execute module F09>
#parameter                  : user_name , datas_gadget , datas_gadget_pinjam , history_kembalian , ID_kembalian , pernah_pinjam
#return value               : datas_gadget , datas_gadget_pinjam , history_kembalian , ID_kembalian

#minta                      : demand consumable <execute module F10>
#parameter                  : user_name , datas_consume , history_minta , ID_minta
#return value               : datas_consume , history_minta , ID_minta


#Dictionaries
#header_gadget , header_consume                                     : list of str
#datas_gadget , datas_consume , datas_gadget_pinjam                 : matrix
#datas_gadget_id , datas_gadget_name , datas_consume_id             : list of str
#datas_gadget_jumlah , datas_consume_jumlah , datas_gadget_tahun    : list of integer
#command , cek_id                                                   : str
#pernah_pinjam                                                      : boolean
#nomor_return , index_id                                            : integer
#tanggal_pinjam , tanggal_return , tanggal_consume                  : str
#jumlah_pinjam , jumlah_return , jumlah_consume                     : integer



def validasi_pinjamgadget(datas_gadget_id , datas_gadget_jumlah):                                                  #validasi value tiap atribut peminjaman gadget
    cek = 0
    while cek < 2:
        cek = 0
        cek_id = input('Masukan ID item: ').upper()
        tanggal_pinjam = input('Tanggal peminjaman (DD/MM/YYYY): ')
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
            elif jumlah_pinjam > datas_gadget_jumlah[index_id]:
                print('Jumlah yg diinginkan berlebihan, stok tidak cukup! Silahkan coba lagi')
            else:
                cek += 1

    return tanggal_pinjam , jumlah_pinjam , index_id

def validasi_balikgadget(datas_gadget_pinjam):                                                                     #validasi value tiap atribut pengembalian gadget
    cek = 0
    while cek < 2:
        cek = 0
        try :
            nomor_return = int(input("Masukan nomor peminjaman: "))
        except ValueError:
            print("Masukan nomor salah, silahkan coba lagi")
            continue

        tanggal_return = input("Tanggal pengembalian (DD/MM/YYYY): ")

        try :
            jumlah_return = int(input("Jumlah yang ingin dibalikkan: "))
        except ValueError:
            print("Masukan jumlah salah, silahkan coba lagi")
            continue

        if nomor_return > len(datas_gadget_pinjam['nama']) :
            print('Nomor tidak ada , silahkan coba lagi')
        else:
            index_id = nomor_return-1
            cek += 1
            if jumlah_return <= 0:
                print('Masukan tidak diterima , silahkan coba lagi')
            elif jumlah_return > datas_gadget_pinjam['jumlah'][index_id]:
                print('jumlah yang ingin dikembalikan berlebihan, silahkan coba lagi')
            else:
                cek += 1
    return tanggal_return , jumlah_return , index_id

def validasi_mintaconsumable(datas_consume_id , datas_consume_jumlah):                                             #validasi value tiap atribut consumable
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




def pinjam(user_name , datas_gadget , datas_gadget_pinjam , history_pinjam , ID_pinjam):
    #list datas secondary (gadget) -> untuk mengecek keberadaan item gadget
    datas_gadget_id     = [data[0] for data in datas_gadget]
    datas_gadget_jumlah = [data[3] for data in datas_gadget]

    tanggal_pinjam, jumlah_pinjam, index_id = validasi_pinjamgadget(datas_gadget_id , datas_gadget_jumlah)               #VALIDASI DATA
    pernah_pinjam = True

    #gadget dipinjam dari datas_gadget
    print(f"Item {datas_gadget[index_id][1]} (x{jumlah_pinjam}) berhasil dipinjam!")
    datas_gadget[index_id][3] -= jumlah_pinjam

    #gadget tercatat ke datas_gadget_pinjam
    if datas_gadget[index_id][1] not in datas_gadget_pinjam['nama']:
        datas_gadget_pinjam['nama'].append(datas_gadget[index_id][1])
        datas_gadget_pinjam['jumlah'].append(jumlah_pinjam)

    else :
        index_barang = datas_gadget_pinjam['nama'].index(datas_gadget[index_id][1])
        datas_gadget_pinjam['jumlah'][index_barang] += jumlah_pinjam

    #gadget tercatat ke history_pinjam
    ID_pinjam += 1
    new_datas = [ID_pinjam , user_name , datas_gadget[index_id][1] , tanggal_pinjam , jumlah_pinjam]
    history_pinjam.append(new_datas)

    return datas_gadget , datas_gadget_pinjam , history_pinjam , ID_pinjam , pernah_pinjam


def kembalikan(user_name , datas_gadget , datas_gadget_pinjam , history_kembalian , ID_kembalian , pernah_pinjam):
    #list datas secondary (gadget) -> untuk mengecek keberadaan item gadget
    datas_gadget_name   = [data[1] for data in datas_gadget]

    if pernah_pinjam == False:                                                              #belum terjadi peminjaman gadget
        print("Belum ada peminjaman")
        return

    #list gadget yang dipinjam
    for i in range(len(datas_gadget_pinjam['nama'])):
        print(f"{i+1}. {datas_gadget_pinjam['nama'][i]} (x{datas_gadget_pinjam['jumlah'][i]})")


    tanggal_return, jumlah_return, index_id = validasi_balikgadget(datas_gadget_pinjam)     #VALIDASI DATA

    print(f"Item {datas_gadget_pinjam['nama'][index_id]} (x{jumlah_return}) telah dikembalikan")

    #gadget keluar dari datas_gadget_pinjam
    datas_gadget_pinjam['jumlah'][index_id] -= jumlah_return

    #gadget kembali ke datas_gadget
    index_barang = datas_gadget_name.index(datas_gadget_pinjam['nama'][index_id])           #letak indeks gadget hasil pinjaman pada list gadget
    datas_gadget[index_barang][3] += jumlah_return                                          #stok gadget bertambah setelah dikembalikan

    #gadget tercatat ke history_kembalian
    ID_kembalian += 1
    new_datas = [ID_kembalian , user_name , datas_gadget_pinjam['nama'][index_id] , tanggal_return , jumlah_return]
    history_kembalian.append(new_datas)

    #kondisi ketika gadget telah dikembalikan semuanya
    if datas_gadget_pinjam['jumlah'][index_id] == 0 :
        print(f"Selamat! Item {datas_gadget_pinjam['nama'][index_id]} telah dikembalikan semua!")
        datas_gadget_pinjam['nama'].remove(datas_gadget_pinjam['nama'][index_id])           #menghapus nama gadget dengan value kosong
        datas_gadget_pinjam['jumlah'].remove(0)                                             #menghapus jumlah gadget bernilai 0


    return datas_gadget , datas_gadget_pinjam , history_kembalian , ID_kembalian


def minta(user_name , datas_consume , history_minta , ID_minta):
    #list datas secondary (consumable)
    datas_consume_id = [data[0] for data in datas_consume]
    datas_consume_jumlah = [data[3] for data in datas_consume]

    jumlah_consume, tanggal_consume, index_id = validasi_mintaconsumable(datas_consume_id , datas_consume_jumlah)        #VALIDASI DATA

    print(f"Item {datas_consume[index_id][1]} (x{jumlah_consume}) telah berhasil diambil!")
    datas_consume[index_id][3] -= jumlah_consume                                                                         #consumable terambil dari stok consumable

    #gadget tercatat ke history_kembalian
    ID_minta += 1
    new_datas = [ID_minta , user_name , datas_consume[index_id][1] , tanggal_consume , jumlah_consume]
    history_minta.append(new_datas)

    return datas_consume , history_minta , ID_minta
