# Program main.py
# Simulates an item inventory system within the given specification

# Dependencies
import argparse
import item_interaction
import database_io
import cari_item

# Dictionary
#

# Algorithm
parser = argparse.ArgumentParser()
parser.add_argument("foldername", help="load a folder with the specified name", type=str)
folder = parser.parse_args()
consumable_raw, consumable_history_raw, gadget_raw,\
    gadget_borrow_history_raw, gadget_return_history_raw, user_raw = database_io.load(folder.foldername)

consum_header = consumable_raw.pop(0)
consum_hist_header = consumable_history_raw.pop(0)
gadget_header = gadget_raw.pop(0)
gadget_borrow_header = gadget_borrow_history_raw.pop(0)
gadget_return_header = gadget_return_history_raw.pop(0)
user_header = user_raw.pop(0)

consumable = database_io.change_data_type("consum", consumable_raw)
consumable_history = database_io.change_data_type("consum_history", consumable_history_raw)
gadget = database_io.change_data_type("gadget", gadget_raw)
gadget_borrow_history = database_io.change_data_type("gadget_borrow", gadget_borrow_history_raw)
gadget_return_history = database_io.change_data_type("gadget_return", gadget_return_history_raw)
user = database_io.change_data_type("user", user_raw)

consum_data = []
consum_hist_data = []
gadget_data = []
gadget_borrow_hist_data = []
gadget_return_hist_data = []
user_data = []

datas_gadget_pinjam = {'nama': [], 'jumlah': []}
pernah_pinjam = False
id_pinjam, id_kembalian, id_minta = 0, 0, 0

print("Selamat datang ke sistem penyimpanan item Doremonangis!")
print('''  
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀
            ⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄
            ⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇
            ⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷
            ⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃
            ⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀
            ⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀
            ⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁
            ''')

while True:
    command = input("Masukkan perintah: ")

    if command == "register":
        pass
    elif command == "login":
        pass
    elif command == "cari_item_rarity":
        cari_item.carirarity(gadget)
    elif command == "cari_item_tahun":
        cari_item.caritahun(gadget)
    elif command == "tambah_item":
        gadget, consumable = item_interaction.add_item(gadget, consumable)
    elif command == "hapus_item":
        gadget, consumable = item_interaction.delete_item(gadget, consumable)
    elif command == "ubah_jumlah_item":
        gadget, consumable = item_interaction.modify_item_amount(gadget, consumable)
    elif command == "pinjam_gadget":
        pass
    elif command == "kembalikan_gadget":
        pass
    elif command == "minta_consumable":
        pass
    elif command == "riwayat_pinjam_gadget":
        pass
    elif command == "riwayat_pengembalian_gadget":
        pass
    elif command == "riwayat_minta_consumable":
        pass
    elif command == "save":
        folder_name = input("Masukkan nama folder penyimpanan: ")

        consum_data.append(consum_header)
        consum_hist_data.append(consum_hist_header)
        gadget_data.append(gadget_header)
        gadget_borrow_hist_data.append(gadget_borrow_header)
        gadget_return_hist_data.append(gadget_return_header)
        user_data.append(user_header)

        consum_data += consumable
        consum_hist_data += consumable_history
        gadget_data += gadget
        gadget_borrow_hist_data += gadget_borrow_history
        gadget_return_hist_data += gadget_return_history
        user_data += user

        consum_csv = database_io.revert_data_type(consum_data)
        consum_hist_csv = database_io.revert_data_type(consum_hist_data)
        gadget_csv = database_io.revert_data_type(gadget_data)
        gadget_borrow_csv = database_io.revert_data_type(gadget_borrow_hist_data)
        gadget_return_csv = database_io.revert_data_type(gadget_return_hist_data)
        user_csv = database_io.revert_data_type(user_data)

        database_io.save(folder_name, "consumable.csv", consum_csv)
        database_io.save(folder_name, "consumable_history.csv", consum_hist_csv)
        database_io.save(folder_name, "gadget.csv", gadget_csv)
        database_io.save(folder_name, "gadget_borrow_history.csv", gadget_borrow_csv)
        database_io.save(folder_name, "gadget_return_history.csv", gadget_return_csv)
        database_io.save(folder_name, "user.csv", user_csv)

        print(f"Data telah disimpan di folder {folder_name}.")
    elif command == "help":
        pass
    elif command == "exit":
        break
    else:
        print("Command tidak valid! Harap ulangi kembali.")
