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

history_pinjam = [["1","U1","G1","18/04/2022",25],
                 ["2","U2","G2","19/04/2022",10],
                 ["3","U3","G3","22/04/2022",2],
                 ["4","U4","G4","20/04/2022",5],
                 ["5","U5","G5","02/11/1942",20],
                 ["6","U6","G6","21/04/2022",10]]

history_kembalian = [["1","1","18/04/2022"],
             ["2","2","19/04/2022"],
             ["3","3","22/04/2022"],
             ["4","4","20/04/2022"],
             ["5","5","21/04/2022"],
             ["6","1","20/04/2023"]]

user = [["U1","parker04","Peter Parker"],
        ["U2","visionwanda","Wanda Vision"],
        ["U3","zeuresius","Yoga"],
        ["U4","x(","Reza"],
        ["U5","dendong","Deen"],
        ["U6","vierimansyl","vieri"]]

gadget = [["G1","Gateway to Anywhere"],
          ["G2","Baling Bambu"],
          ["G3","Laptop"],
          ["G4","Machine Learning"],
          ["G5","Buku Sobbota"],
          ["G6","iphone 20"]]

consumable = [["C1","kerak telor","pake telur",32,"C"],
              ["C2","KFC","pake ayam",16,"S"],
              ["C3","rujak","pake buah",23,"A"],
              ["C4","takjil","pake air",50,"B"],
              ["C5","dodol","pake santan",35,"B"],
              ["C6","kolak pisang","pake santan juga","15","A"]]

history_minta = [["1","U1","C1","22/04/2022",14],
                  ["2","U2","C2","23/04/2022",9],
                  ["3","U3","C3","19/04/2022",18],
                  ["4","U4","C4","21/04/2022",20],
                  ["5","U5","C5","24/04/2022",13],
                  ["6","U1","C3","26/04/2025",5]]




# F11 : Melihat riwayat peminjaman gadget
# Diasumsikan pada data terdapat 5 entry dan akan dikeluarkan 5 entry tersebut terurut dari tanggal peminjaman terbaru


def riwayatPinjamGadget (history_pinjam):

    cek = True
    indeks = -5
    panjang = 0
    command = "Y"

    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple
    history_pinjam.sort(key = lambda x: time.mktime(datetime.strptime(x[3], '%d/%m/%Y').timetuple()), reverse=True)
    
    print()
    print(history_pinjam)

    print("Riwayat Peminjaman: ")

    while cek and command == "Y":
        command = ""
        cek_command = False
        indeks += 5
        if indeks > len(history_pinjam):
            indeks -= 5
            panjang = len(history_pinjam) - indeks
            cek     = False
        elif indeks == len(history_pinjam):
            print("riwayat sudah habis")
            break
        else:
            panjang += 5

        for i in range(indeks , indeks + panjang , 1):

            print()
            print("Id peminjaman\t\t: ", history_pinjam[i][0])   
            print("Nama pengambil\t\t: ", list(filter(lambda x: x[0] == history_pinjam[i][1], user))[0][2])  # Mengambil nama peminjam dari id user melalui data peminjaman
            print("Nama Gadget\t\t: ", list(filter(lambda x: x[0] == history_pinjam[i][2], gadget))[0][1])   # Mengambil nama gadget dari id gadget melalui data peminjaman
            print("Tanggal peminjaman\t: ", history_pinjam[i][3])
            print("Jumlah\t\t\t: ", history_pinjam[i][4])
            print()
            if not cek :
                print("riwayat sudah habis")
                break

        while command != "Y" or command != "N" and not(cek_command):
            command = input("Next? [Y/N]: ").upper()
            if (command == "Y" or command == "N"):
                cek_command = True
            else:
                 print("Masukan salah. Silahkan coba lagi")

# riwayatPinjamGadget(history_pinjam)


# F12 : Melihat Riwayat Pengembalian Gadget 
# Diasumsikan pada data terdapat 5 entry dan akan dikeluarkan 5 entry data tersebut terurut dari tanggal peminjaman terbaru

def riwayatBalikGadget (history_kembalian): 
    
    cek = True
    indeks = -5
    panjang = 0
    command = "Y"

    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple
    history_kembalian.sort(key = lambda x: time.mktime(datetime.strptime(x[2], '%d/%m/%Y').timetuple()), reverse=True)
    
    print()
    print(history_kembalian)

    print("Riwayat Pengembalian: ")

    while cek and command == "Y":
        command = ""
        cek_command = False
        indeks += 5
        if indeks > len(history_kembalian):
            indeks -= 5
            panjang = len(history_pinjam) - indeks
            cek     = False
        elif indeks == len(history_kembalian):
            print("riwayat sudah habis")
            break
        else:
            panjang += 5

        for i in range(indeks , indeks + panjang , 1):
            peminjaman = list(filter(lambda x: x[0] == history_kembalian[i][1], history_pinjam))[0]   # Mengambil data peminjaman dari list data pengembalian (data balik)
            print()
            print("Id pengembalian\t\t: ", history_kembalian[i][0])
            print ("Nama pengambil\t\t: ", list(filter(lambda x: x[0] == peminjaman[1], user))[0][2])   # Mengambil nama peminjam dari id user dari data peminjaman
            print("Nama Gadget\t\t: ", list(filter(lambda x: x[0] == peminjaman[2], gadget))[0][1])     # Mengambil nama gadget dari id gadget dari data peminjaman
            print("Tanggal Peminjaman\t: ", history_kembalian[i][2])
            print()

            if not cek :
                print("riwayat sudah habis")
                break

        while command != "Y" or command != "N" and not(cek_command):
            command = input("Next? [Y/N]: ").upper()
            if (command == "Y" or command == "N"):
                    cek_command = True
            else:
                print("Masukan salah. Silahkan coba lagi")


#riwayatBalikGadget(history_kembalian)



# F13 Melihat riwayat pengambilan consumable 
# Diasumsikan pada data terdapat 5 entry dan akan dikeluarkan 5 entry data tersebut terurut dari tanggal peminjaman terbaru

def riwayatConsumable(history_minta):

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
        elif indeks == len(history_minta):
            print("riwayat sudah habis")
            break
        else:
            panjang += 5

        for i in range(indeks , indeks + panjang , 1):
            print()
            print("Id Pengambilan\t\t: ",history_minta[i][0])
            print("Nama Pengambil\t\t: ", list(filter(lambda x: x[0] == history_minta[i][1], user))[0][2])             # Mengambil nama pengambil dari id user dari data peminjaman
            print("Nama Consumable\t\t: ", list(filter(lambda x: x[0] == history_minta[i][2], consumable))[0][1])      # Mengambil nama consumable dari id consumable dari data "consumable"
            print("Tanggal Pengambilan\t: ", history_minta[i][3])
            print("Jumlah\t\t\t: ", history_minta[i][4])
            print()
            
            if not cek :
                print("riwayat sudah habis")
                break

        while command != "Y" or command != "N" and not(cek_command):
            command = input("Next? [Y/N]: ").upper()
            if (command == "Y" or command == "N"):
                    cek_command = True
            else:
                print("Masukan salah. Silahkan coba lagi")


#riwayatConsumable(history_minta)