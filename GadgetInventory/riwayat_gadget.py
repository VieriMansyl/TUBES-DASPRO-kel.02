import time
from datetime import datetime

# Membuat program untuk melihat riwayat peminjaman,pengembalian gadget dan riwayat pengembalian consumable
# Coder : 16520356

# Kamus 
# datapinjam , databalik, dataconsumable = Array of Data
# user, gadget, consumable = Array of Data
# riwayatPinjamGadget , riwayatBalikGadget, riwayatConsumable = function 
# list, filter, = fungsi bawaan python
# Tanggal peminjaman, pengembalian, riwayat consumable = string 


# Kamus untuk Array of Data
# 1, 2, 3, 4, 5, dst = Id peminjaman ( dibuat secara otomatis )
# 1, 2, 3, 4, 5, dst = Id pengembalian ( dibuat secara otomatis )
# 1, 2, 3, 4, 5, dst = Id riwayat consumable ( dibuat secara otomatis )
# U1, U2, U3, U4, U5, dst = Contoh untuk Id user agar bisa mengakses data "user"
# G1, G2, G3, G4, G5, dst = Contoh untuk Id Gadget agar bisa mengakses data "gadget"
# C1, C2, C2, C4, C5, dst = Contoh untuk Id dari consumable agar bisa mengakses data "consumable"


# F11 : Melihat riwayat peminjaman gadget
'''
#yg ada
data_history        = [ID_kembalian , id_peminjaman[indeks_ID_pinjam] , tanggal_return , jumlah_return]
user            = [identity, nama , username,  password, alamat, role]
#yg pengen
new_datas = [ID_kembalian , user_name , pinjaman_user['nama_gadget'][index_id] , tanggal_return , jumlah_return]
'''
def konversi_history_pinjam(history_pinjam , user, gadget):
    cek_identity = [data[0] for data in user]
    cek_username = [data[2] for data in user]
    for i in range(len(history_pinjam)):
        indeks = cek_identity.index(history_pinjam[i][1])
        history_pinjam[i][1] = cek_username[indeks]
    
    id_gadget   = [data[0] for data in gadget]
    nama_gadget = [data[1] for data in gadget]
    for i in range(len(gadget)):
        indeks = id_gadget.index(history_pinjam[i][2])
        history_pinjam[i][2] = nama_gadget[indeks]
    return history_pinjam



def riwayatPinjamGadget (history_pinjam,user,gadget):

    cek = True
    indeks = -5
    panjang = 0
    command = "Y"

    history_pinjam = konversi_history_pinjam(history_pinjam, user, gadget)
    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple
    history_pinjam.sort(key = lambda x: time.mktime(datetime.strptime(x[3], '%d/%m/%Y').timetuple()), reverse=True)
    
    print("Riwayat Peminjaman: ")

    while cek and command == "Y":
        command = ""
        cek_command = False
        indeks += 5
        if indeks > len(history_pinjam):
            indeks -= 5
            panjang = len(history_pinjam) - indeks
            cek     = False
        else:
            panjang += 5

        for i in range(indeks , indeks + panjang , 1):
            if i == len(history_pinjam):
                print("Riwayat sudah habis")
                return

            print()
            print("Id peminjaman\t\t: ", history_pinjam[i][0])   
            print("Nama pengambil\t\t: ", list(filter(lambda x: x[0] == history_pinjam[i][1], user))[0][1])  # Mengambil nama peminjam dari id user melalui data peminjaman
            print("Nama Gadget\t\t: ", list(filter(lambda x: x[0] == history_pinjam[i][2], gadget))[0][1])   # Mengambil nama gadget dari id gadget melalui data peminjaman
            print("Tanggal peminjaman\t: ", history_pinjam[i][3])
            print("Jumlah\t\t\t: ", history_pinjam[i][4])
            print()
            

        while command != "Y" or command != "N" and not(cek_command):
            command = input("Next? [Y/N]: ").upper()
            if (command == "Y"):
                cek_command = True
            elif (command == "N"): 
                break
            else: # Masukkan selain Y dan N
                print("Masukan Salah. Silahkan coba lagi.")


# F12 : Melihat Riwayat Pengembalian Gadget 

def riwayatBalikGadget (history_kembalian,user,gadget,history_pinjam): 
    
    cek = True
    indeks = -5
    panjang = 0
    command = "Y"

    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple
    history_kembalian.sort(key = lambda x: time.mktime(datetime.strptime(x[2], '%d/%m/%Y').timetuple()), reverse=True)
    

    print("Riwayat Pengembalian: ")

    while cek and command == "Y":
        command = ""
        cek_command = False
        indeks += 5
        if indeks > len(history_kembalian):
            indeks -= 5
            panjang = len(history_kembalian) - indeks
            cek     = False
        else:
            panjang += 5

        for i in range(indeks , indeks + panjang , 1):
            if i == len(history_kembalian):
                print("Riwayat sudah habis")
                return

            peminjaman = list(filter(lambda x: x[0] == history_kembalian[i][1], history_pinjam))[0]   # Mengambil data peminjaman dari list data pengembalian (history_kembalian)
            print()
            print("Id pengembalian\t\t: ", history_kembalian[i][0])
            print ("Nama pengambil\t\t: ", list(filter(lambda x: x[0] == peminjaman[1], user))[0][1])   # Mengambil nama peminjam dari id user dari data peminjaman
            print("Nama Gadget\t\t: ", list(filter(lambda x: x[0] == peminjaman[2], gadget))[0][1])     # Mengambil nama gadget dari id gadget dari data peminjaman
            print("Tanggal Pengembalian\t: ", history_kembalian[i][2])
            print()

        while command != "Y" or command != "N" and not(cek_command):
            command = input("Next? [Y/N]: ").upper()
            if (command == "Y"):
                    cek_command = True
            elif (command == "N"):
                break
            else: 
                print("Masukan Salah. Silahkan coba lagi.")



# F13 Melihat riwayat pengambilan consumable 

def riwayatConsumable(history_minta,user,consumable):

    cek = True
    indeks = -5
    panjang = 0
    command = "Y"

    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple
    history_minta.sort(key = lambda x: time.mktime(datetime.strptime(x[3], '%d/%m/%Y').timetuple()), reverse=True)

    print("Riwayat pengambilan consumable")
    
    while cek and command == "Y":
        cek_command = False
        indeks += 5
        if indeks > len(history_minta):
            indeks -= 5
            panjang = len(history_minta) - indeks
            cek     = False
        else:
            panjang += 5

        for i in range(indeks , indeks + panjang , 1):
            if i == len(history_minta):
                print("Riwayat sudah habis")
                return

            print()
            print("Id Pengambilan\t\t: ",history_minta[i][0])
            print("Nama Pengambil\t\t: ", list(filter(lambda x: x[0] == history_minta[i][1], user))[0][1])        # Mengambil nama pengambil dari id user dari data peminjaman      
            print("Nama Consumable\t\t: ", list(filter(lambda x: x[0] == history_minta[i][2], consumable))[0][1]) # Mengambil nama consumable dari id consumable dari data "consumable"
            print("Tanggal Pengambilan\t: ", history_minta[i][3])
            print("Jumlah\t\t\t: ", history_minta[i][4])
            print()
            
        while command != "Y" or command != "N" and not(cek_command):
            command = input("Next? [Y/N]: ").upper()
            if (command == "Y"):
                cek_command = True
            elif (command == "N"):
                break
            else:
                print("Masukan Salah. Silahkan coba lagi")