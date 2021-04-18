#Contributor : Vieri Mansyl - 16520056

#Function
#arraydata_to_realvalue     : converts each datas from csv into a data which holds its real value
#return value               : arr_copy

#line_to_data               : converts a string into multiple data values
#return value               : array_of_data

#csv_to_data                : converts csv file into array(s)
#return value               : header, datas

#validasi_pinjamgadget      : validate each attributes of 'borrow gadget(s)' module - F08
#return value               : cek_id , tanggal_pinjam , jumlah_pinjam , index_id

#validasi_balikgadget       : validate each attributes of 'return gadget(s)' module - F09
#return value               : nomor_return , tanggal_return , jumlah_return , index_id

#validasi_mintaconsumeable  : validate each attributes of 'request consumable(s)' module - F10
#return value               : cek_id , jumlah_consume , tanggal_consume , index_id

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


def arraydata_to_realvalue(file_name,array_data):
    arr_copy = array_data[:]
    if file_name == "data_tes":
        for i in range(6):
            if(i == 3 or i == 5):
                arr_copy[i] = int(arr_copy[i])
    elif file_name == "consume_tes":
        for i in range(5):
            if i == 3:
                arr_copy[i] = int(arr_copy[i])
    return arr_copy

def line_to_data(line):
    raw_array_of_data = line.split(";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def csv_to_data(file_name):
    if file_name == "data_tes":
        f = open("data_tes.csv","r")
    elif file_name == "consume_tes":
        f = open("consume_tes.csv","r")
    
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = line_to_data(raw_header)
    datas = []

    for line in lines:
        array_of_data = line_to_data(line)
        real_values = arraydata_to_realvalue(file_name , array_of_data)
        datas.append(real_values)
    
    return header, datas

def validasi_pinjamgadget():                                                                    #validasi value tiap atribut peminjaman gadget
    cek = 0
    while cek < 2:
        cek = 0
        cek_id = input('Masukan ID item: ').upper()
        tanggal_pinjam = input('Tanggal peminjaman (DD/MM/YYYY): ')
        try :
            jumlah_pinjam = int(input("Jumlah peminjaman: "))
        except ValueError:
            print("masukan salah, silahkan coba lagi")
            continue

        if cek_id not in datas_gadget_id:
            print('id tidak ada , silahkan input kembali')
        else:
            index_id = datas_gadget_id.index(cek_id)
            cek += 1
            if jumlah_pinjam <= 0:
                print('masukan tidak diterima ; jumlah <= 0')
            elif datas_gadget_jumlah[index_id] == 0:
                print('stok barang udah habis')
            elif jumlah_pinjam > datas_gadget_jumlah[index_id]:
                print('jumlah yg diinginkan kelebihan, stok tidak cukup')
            else:
                cek += 1

    return cek_id , tanggal_pinjam , jumlah_pinjam , index_id

def validasi_balikgadget():                                                                     #validasi value tiap atribut pengembalian gadget
    cek = 0
    while cek < 2:
        cek = 0
        try :
            nomor_return = int(input("Masukan nomor peminjaman: "))
        except ValueError:
            print("masukan nomor salah, silahkan coba lagi")
            continue

        tanggal_return = input("Tanggal pengembalian (DD/MM/YYYY): ")

        try :
            jumlah_return = int(input("Jumlah yang ingin dibalikkan: "))
        except ValueError:
            print("masukan jumlah salah, silahkan coba lagi")
            continue

        if nomor_return > len(datas_gadget_pinjam['nama']) :
            print('nomor tidak ada , silahkan input kembali')
        else:
            index_id = nomor_return-1
            cek += 1
            if jumlah_return <= 0:
                print('masukan tidak diterima ; jumlah return <= 0')
            elif jumlah_return > datas_gadget_pinjam['jumlah'][index_id]:
                print('jumlah kelebihan, silahkan input kembali')
            else:
                cek += 1
    return nomor_return , tanggal_return , jumlah_return , index_id

def validasi_mintaconsumeable():                                                                #validasi value tiap atribut consumable
    cek = 0
    while cek < 2:
        cek = 0

        cek_id = input('Masukan ID item: ').upper()

        try :
            jumlah_consume = int(input('Jumlah: '))
        except ValueError:
            print("masukan salah, silahkan coba lagi")
            continue

        tanggal_consume = input("Tanggal permintaan (DD/MM/YYYY): ")

        if cek_id not in datas_consume_id:
            print('id tidak ada , silahkan input kembali')
        else:
            index_id = datas_consume_id.index(cek_id)
            cek += 1
            if jumlah_consume <= 0:
                print('masukan tidak diterima ; jumlah <= 0')
            elif datas_consume_jumlah[index_id] == 0:
                print('stok barang udah habis')
            elif jumlah_consume > datas_consume_jumlah[index_id]:
                print('jumlah yg diinginkan kelebihan, stok tidak cukup')
            else:
                cek += 1
    return cek_id , jumlah_consume , tanggal_consume , index_id


#for gadget
header_gadget, datas_gadget = csv_to_data('data_tes')
#list datas secondary
datas_gadget_id = [data[0] for data in datas_gadget]
datas_gadget_name = [data[1] for data in datas_gadget]
datas_gadget_jumlah = [data[3] for data in datas_gadget]
datas_gadget_tahun = [data[5] for data in datas_gadget]
datas_gadget_pinjam = {'nama': [] , 'jumlah' : []}                                              #buku peminjaman

#for consumable
header_consume, datas_consume = csv_to_data('consume_tes')
#list datas secondary
datas_consume_id = [data[0] for data in datas_consume]
datas_consume_jumlah = [data[3] for data in datas_consume]

#inisialisasi
command = ''
pernah_pinjam = False       #penentu ketika belum terjadi peminjaman gadget

while command != 'berhenti':
    command = input('>>>')


    if command == "pinjam":                                                                     #PEMINJAMAN GADGET
        pernah_pinjam = True
        cek_id, tanggal_pinjam, jumlah_pinjam, index_id = validasi_pinjamgadget()               #VALIDASI DATA
        
        #gadget keluar dari datas_gadget
        print(f"Item {datas_gadget[index_id][1]} (x{jumlah_pinjam}) berhasil dipinjam!")
        datas_gadget[index_id][3] -= jumlah_pinjam

        #gadget tercatat ke datas_gadget_pinjam
        if datas_gadget[index_id][1] not in datas_gadget_pinjam['nama']:
            datas_gadget_pinjam['nama'].append(datas_gadget[index_id][1])
            datas_gadget_pinjam['jumlah'].append(jumlah_pinjam)
        else :
            index_barang = datas_gadget_pinjam['nama'].index(datas_gadget[index_id][1])
            datas_gadget_pinjam['jumlah'][index_barang] += jumlah_pinjam

    elif command == "kembalikan":                                                               #PENGEMBALIAN GADGET
        if pernah_pinjam == False:                                                              #belum terjadi peminjaman gadget
            print("Belum ada peminjaman")
            continue

        #list gadget yang dipinjam
        for i in range(len(datas_gadget_pinjam['nama'])):
            print(f"{i+1}. {datas_gadget_pinjam['nama'][i]} (x{datas_gadget_pinjam['jumlah'][i]})")

        nomor_return, tanggal_return, jumlah_return, index_id = validasi_balikgadget()          #VALIDASI DATA

        print(f"Item {datas_gadget_pinjam['nama'][index_id]} (x{jumlah_return}) telah dikembalikan")

        #gadget keluar dari datas_gadget_pinjam
        datas_gadget_pinjam['jumlah'][index_id] -= jumlah_return

        #gadget kembali ke datas_gadget
        index_barang = datas_gadget_name.index(datas_gadget_pinjam['nama'][index_id])
        datas_gadget[index_barang][3] += jumlah_return                                          #stok gadget bertambah setelah dikembalikan

        #saat gadget dikembalikan semuanya
        if datas_gadget_pinjam['jumlah'][index_id] == 0 :
            print(f"Item {datas_gadget_pinjam['nama'][index_id]} telah dikembalikan semua!")
            datas_gadget_pinjam['nama'].remove(datas_gadget_pinjam['nama'][index_id])           #menghapus nama gadget dengan value kosong
            datas_gadget_pinjam['jumlah'].remove(0)                                             #menghapus jumlah gadget bernilai 0

    elif command == "minta":                                                                    #PERMINTAAAN CONSUMABLE
        cek_id, jumlah_consume, tanggal_consume, index_id = validasi_mintaconsumeable()         #VALIDASI DATA

        print(f"Item {datas_consume[index_id][1]} (x{jumlah_consume}) telah berhasil diambil!")
        datas_consume[index_id][3] -= jumlah_consume                                            #consumable terambil dari stok consumable
        
    elif command == "berhenti":                                                                 #TERMINASI PROGRAM
        break
