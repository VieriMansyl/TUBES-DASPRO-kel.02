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
# 1, 2, 3, 4, 5 = Id peminjaman ( dibuat secara otomatis )
# 1, 2, 3, 4, 5 = Id pengembalian ( dibuat secara otomatis )
# 1, 2, 3, 4, 5 = Id riwayat consumable ( dibuat secara otomatis )
# U1, U2, U3, U4, U5 = Contoh untuk Id user agar bisa mengakses data "user"
# G1, G2, G3, G4, G5 = Contoh untuk Id Gadget agar bisa mengakses data "gadget"
# C1, C2, C2, C4, C5 = Contoh untuk Id dari consumable agar bisa mengakses data "consumable"




# Contoh array data untuk testing 
# Ini contoh aja ya ges, kalo mau ubah juga bisa

datapinjam = [["1","U1","G1","18/04/2022",25],
             ["2","U2","G2","19/04/2022",10],
             ["3","U3","G3","22/04/2022",2],
             ["4","U4","G4","20/04/2022",5],
             ["5","U5","G5","21/04/2022",10]]

databalik = [["1","1","18/04/2022"],
             ["2","2","19/04/2022"],
             ["3","3","22/04/2022"],
             ["4","4","20/04/2022"],
             ["5","5","21/04/2022"]]

user = [["U1","parker04","Peter Parker"],
        ["U2","visionwanda","Wanda Vision"],
        ["U3","zeuresius","Yoga"],
        ["U4","x(","Reza"],
        ["U5","dendong","Deen"]]

gadget = [["G1","Gateway to Anywhere"],
          ["G2","Baling Bambu"],
          ["G3","Laptop"],
          ["G4","Machine Learning"],
          ["G5","Buku Sobbota"]]

consumable = [["C1","kerak telor","pake telur",32,"C"],
              ["C2","KFC","pake ayam",16,"S"],
              ["C3","rujak","pake buah",23,"A"],
              ["C4","takjil","pake air",50,"B"],
              ["C5","dodol","pake santan",35,"B"]]

dataconsumable = [["1","U1","C1","22/04/2022",14],
                     ["2","U2","C2","23/04/2022",9],
                     ["3","U3","C3","19/04/2022",18],
                     ["4","U4","C4","21/04/2022",20],
                     ["5","U5","C5","24/04/2022",13]]


# F11 : Melihat riwayat peminjaman gadget
# Diasumsikan pada data terdapat 5 entry dan akan dikeluarkan 5 entry tersebut terurut dari tanggal peminjaman terbaru


def riwayatPinjamGadget ():


    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple

    datapinjam.sort(key = lambda x: time.mktime(datetime.strptime(x[3], '%d/%m/%Y').timetuple()), reverse=True)  
  
    print("Riwayat Peminjaman: ")
    for i in range(len(datapinjam)):
        print()
        print("Id peminjaman\t\t: ", datapinjam[i][0])   
        print("Nama pengambil\t\t: ", list(filter(lambda x: x[0] == datapinjam[i][1], user))[0][2])  # Mengambil nama peminjam dari id user melalui data peminjaman
        print("Nama Gadget\t\t: ", list(filter(lambda x: x[0] == datapinjam[i][2], gadget))[0][1])   # Mengambil nama gadget dari id gadget melalui data peminjaman
        print("Tanggal peminjaman\t: ", datapinjam[i][3])
        print("Jumlah\t\t\t: ", datapinjam[i][4])
        print()

riwayatPinjamGadget()


# F12 : Melihat Riwayat Pengembalian Gadget 
# Diasumsikan pada data terdapat 5 entry dan akan dikeluarkan 5 entry data tersebut terurut dari tanggal peminjaman terbaru

def riwayatBalikGadget (): 

    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple

    databalik.sort(key = lambda x: time.mktime(datetime.strptime(x[2], '%d/%m/%Y').timetuple()), reverse=True)

    print("Riwayat Pengembalian:")
    for i in range(len(databalik)):
        peminjaman = list(filter(lambda x: x[0] == databalik[i][1], datapinjam))[0]   # Mengambil data peminjaman dari list data pengembalian (data balik)
        print()
        print("Id pengembalian\t\t: ", databalik[i][0])
        print ("Nama pengambil\t\t: ", list(filter(lambda x: x[0] == peminjaman[1], user))[0][2])   # Mengambil nama peminjam dari id user dari data peminjaman
        print("Nama Gadget\t\t: ", list(filter(lambda x: x[0] == peminjaman[2], gadget))[0][1])     # Mengambil nama gadget dari id gadget dari data peminjaman
        print("Tanggal Peminjaman\t: ", databalik[i][2])
        print()

riwayatBalikGadget()



# F13 Melihat riwayat pengambilan consumable 
# Diasumsikan pada data terdapat 5 entry dan akan dikeluarkan 5 entry data tersebut terurut dari tanggal peminjaman terbaru

def riwayatConsumable():

    # Untuk mensorting descending (dari besar ke kecil, dari tanggal dan tahun dari yang paling baru) 
    # Menggunakan import time, datetime, dan fungsi time tuple

    dataconsumable.sort(key = lambda x: time.mktime(datetime.strptime(x[3], '%d/%m/%Y').timetuple()), reverse=True)

    print("Riwayat pengembalian consumable")
    for i in range(len(dataconsumable)):
        print()
        print("Id Pengambilan\t\t: ",dataconsumable[i][0])
        print("Nama Pengambil\t\t: ", list(filter(lambda x: x[0] == dataconsumable[i][1], user))[0][2])             # Mengambil nama pengambil dari id user dari data peminjaman
        print("Nama Consumable\t\t: ", list(filter(lambda x: x[0] == dataconsumable[i][2], consumable))[0][1])      # Mengambil nama consumable dari id consumable dari data "consumable"
        print("Tanggal Pengambilan\t: ", dataconsumable[i][3])
        print("Jumlah\t\t\t: ", dataconsumable[i][4])
        print()

riwayatConsumable()