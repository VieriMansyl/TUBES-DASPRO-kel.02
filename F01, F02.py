# Login and Register
# Fungsi login dan daftar
# Kontributor : 16520076

# Dictionary
# id, nama, username, password, alamat, role : str

# Fungsi used_name
# Membuat nama yg di-input otomatis kapital
# Parameter : word
# Return value : real_name
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

# Procedure is_underscore
# Menge-cek apakah ada username kembar
# Parameter : x
def is_underscore(x):
    for char in x:
        if char == "_":
            return True

# Procedure username_kembar
# Menge-cek apakah ada username kembar
# Parameter : x
def username_kembar(x):
        for i in range (len(users_data)):
            if x == users_data[i][2]:
                return False
    
# Fungsi register
# Menambahkan user baru ke database
# Parameter : users_data
# Return value : identity, used_name(nama), username,  password, alamat, role
def register(users_data) :
    nama = input("Masukkan nama : ")
    # Huruf kapital otomatis
    used_name(nama)

    username = input("Masukkan username : ")
    # Username kembar
    username_kembar(username)
    # Cek Username tidak boleh kosong & ada yg kembar
    while (username == "") or (username_kembar(username) == False) or (is_underscore(username) == True):
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
        print("Alamat invalid, masukkan alamat lain !")
        alamat = input("Masukkan alamat : ")

    role = "user"
    identity = ("U" + str(len(users_data)+1))
    
    new_user = [identity, used_name(nama), username,  password, alamat, role]

    users_data.append(new_user)
    
    print(f"User {username} berhasil register ke kantong ajaib." )
    
    return users_data

# Procedure Login
# Parameter : users_data
def login(users_data):
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    password_benar = ""
    for i in range (len(users_data)) :
        if users_data[i][2] == username:
            password_benar = users_data[i][3]
    
    if (password_benar == ""): # Username not found
        print("Username belum terdaftar !")
    else:
        while (password) != (password_benar):
            print("Upps, password salah silakan coba lagi !")
            password = input("Masukkan password : ")
        else :
            print("Selamat login berhasil !")
