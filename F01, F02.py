# Login and Register
# Fungsi login dan daftar
# Kontributor : 16520076

# Fungsi register
# Menambahkan user baru ke database

# Dictionary
# id, nama, username, password, alamat, role : str

# ALGORITMA
def register(users_data) :
    nama = input("Masukkan nama : ")
    # Huruf kapital otomatis
    def used_name(word): 
        nameArr = []
        for i in range (len(word)):
            nameArr.append(word[i]) 

        for i in range (len(nameArr)):
            nameArr[i] = (nameArr[i]).lower()

        for i in range (len(nameArr)):
            nameArr[0] = (nameArr[0]).upper()
            if nameArr[i] == ' ':
                nameArr[i+1] = (nameArr[i+1]).upper()
        
        real_name = "".join(nameArr)
        return(real_name)


    username = input("Masukkan username : ")
    # Username kembar
    def username_kembar(x):
        for users in users_data:
            if x == users['username']:
                return False
    # Cek Username tidak boleh kosong & ada yg kembar
    while (username == "") or (username_kembar(username) == False):
        print("Username invalid, masukkan username lain !")
        username = input("Masukkan username : ")

    password = input("Masukkan password : ")
    # Cek password, password tidak boleh kosong
    while (password == ""):
        print("Password invalid, masukkan password lain !")
        password = input("Masukkan password : ")

    alamat = input("Masukkan alamat : ")
    # Cek alamat, tidak boleh kosong
    while (alamat == ""):
        print("Alamat invalid, masukkan a;amat lain !")
        alamat = input("Masukkan alamat : ")

    role = "user"
    identity = (nama[0] + nama[len(nama)-1])
    
    new_user = {"id" : identity, "nama" : used_name(nama), "username" : username, "password" : password, "alamat" : alamat, "role" : role}

    users_data.append(new_user)
    
    print(f"User {username} berhasil register ke kantong ajaib." )

    print(users_data)
    

# Fungsi Login

def login(users_data):
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    password_benar = ""
    for users in users_data :
        if users['username'] == username:
            password_benar = users["password"]
    
    if (password_benar == ""): # Username not found
        print("Username belum terdaftar !")
    else:
        while (password) != (password_benar):
            print("Upps, password salah silakan coba lagi !")
            password = input("Masukkan password : ")
        else :
            print("Selamat login berhasil !")
