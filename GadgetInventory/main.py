# Program main.py
# Simulates an item inventory system within the given specification

# Dependencies
import argparse
import userinfo
import cari_item
import item_interaction
import item_movement
import riwayat_gadget
import database_io
import help_log

# Dictionary
#

# Algorithm
parser = argparse.ArgumentParser()
parser.add_argument("foldername", help="load a folder with the specified name", type=str)
folder = ""

try:
    folder = parser.parse_args()
except SystemExit:
    print("Tidak ada nama file yang diberikan!")
    exit()

consumable_raw, consumable_history_raw, gadget_raw, gadget_borrow_history_raw, \
    gadget_log_raw, gadget_return_history_raw, user_raw = database_io.load(folder.foldername)

consum_header = consumable_raw.pop(0)
consum_hist_header = consumable_history_raw.pop(0)
gadget_header = gadget_raw.pop(0)
gadget_borrow_header = gadget_borrow_history_raw.pop(0)
gadget_log_header = gadget_log_raw.pop(0)
gadget_return_header = gadget_return_history_raw.pop(0)
user_header = user_raw.pop(0)

consumable = database_io.change_data_type("consum", consumable_raw)
consumable_history = database_io.change_data_type("consum_history", consumable_history_raw)
gadget = database_io.change_data_type("gadget", gadget_raw)
gadget_borrow_history = database_io.change_data_type("gadget_borrow", gadget_borrow_history_raw)
gadget_log = database_io.change_data_type("gadget_log", gadget_log_raw)
gadget_return_history = database_io.change_data_type("gadget_return", gadget_return_history_raw)
user = database_io.change_data_type("user", user_raw)

consum_data = []
consum_hist_data = []
gadget_data = []
gadget_borrow_hist_data = []
gadget_log_data = []
gadget_return_hist_data = []
user_data = []

id_pinjam, id_kembalian, id_minta = 0, 0, 0
username = ""
role = ""
identity = ""


def save_csv(consum_datas, consum_hist_datas, gadget_datas, gadget_borrow_hist_datas,
             gadget_log_datas, gadget_return_hist_datas, user_datas):
    folder_name = input("Masukkan nama folder penyimpanan: ")

    consum_datas.append(consum_header)
    consum_hist_datas.append(consum_hist_header)
    gadget_datas.append(gadget_header)
    gadget_borrow_hist_datas.append(gadget_borrow_header)
    gadget_log_datas.append(gadget_log_header)
    gadget_return_hist_datas.append(gadget_return_header)
    user_datas.append(user_header)

    consum_datas += consumable
    consum_hist_datas += consumable_history
    gadget_datas += gadget
    gadget_borrow_hist_datas += gadget_borrow_history
    gadget_log_datas += gadget_log
    gadget_return_hist_datas += gadget_return_history
    user_datas += user

    consum_csv = database_io.revert_data_type(consum_datas)
    consum_hist_csv = database_io.revert_data_type(consum_hist_datas)
    gadget_csv = database_io.revert_data_type(gadget_datas)
    gadget_borrow_csv = database_io.revert_data_type(gadget_borrow_hist_datas)
    gadget_log_csv = database_io.revert_data_type(gadget_log_datas)
    gadget_return_csv = database_io.revert_data_type(gadget_return_hist_datas)
    user_csv = database_io.revert_data_type(user_datas)

    database_io.save(folder_name, "consumable.csv", consum_csv)
    database_io.save(folder_name, "consumable_history.csv", consum_hist_csv)
    database_io.save(folder_name, "gadget.csv", gadget_csv)
    database_io.save(folder_name, "gadget_borrow_history.csv", gadget_borrow_csv)
    database_io.save(folder_name, "gadget_log.csv", gadget_log_csv)
    database_io.save(folder_name, "gadget_return_history.csv", gadget_return_csv)
    database_io.save(folder_name, "user.csv", user_csv)

    print(f"Data telah disimpan di folder {folder_name}.")

print("=================================================================================================")
print("              Selamat datang ke sistem penyimpanan item Doremonangis!                            ")

while True:
    command = input("\nMasukkan perintah: ")

    if command == "reg":
        if role == "admin":
            username, role, identity = userinfo.register(user)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "log":
        username, role, identity = userinfo.login(user)
    elif command == "crare":
        if not role:
            print("Silakan login terlebih dahulu untuk menggunakan perintah ini (perintah : login).")
        else:
            cari_item.carirarity(gadget)
    elif command == "cyear":
        if not role:
            print("Silakan login terlebih dahulu untuk menggunakan perintah ini (perintah : login).")
        else:
            cari_item.caritahun(gadget)
    elif command == "add":
        if role == "admin":
            gadget, consumable = item_interaction.add_item(gadget, consumable)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "delete":
        if role == "admin":
            gadget, consumable = item_interaction.delete_item(gadget, consumable)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "change":
        if role == "admin":
            gadget, consumable = item_interaction.modify_item_amount(gadget, consumable)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "borrow":
        if role == "user":
            gadget, gadget_log, gadget_borrow_history, id_pinjam = item_movement.pinjam(username, gadget, gadget_log,
                                                                                        gadget_borrow_history,
                                                                                        id_pinjam)
        else:
            print("Maaf, perintah ini hanya tersedia untuk user. Silakan login sebagai user (perintah : login).")
    elif command == "return":
        if role == "user":
            gadget, gadget_log, gadget_return_history, id_kembalian , id_pinjam = item_movement.kembalikan(username, gadget,
                                                                                               gadget_log,
                                                                                               gadget_return_history,
                                                                                               id_kembalian,
                                                                                               id_pinjam)
        else:
            print("Maaf, perintah ini hanya tersedia untuk user. Silakan login sebagai user (perintah : login).")
    elif command == "demand":
        if role == "user":
            consumable, consumable_history, id_minta = item_movement.minta(username, consumable, consumable_history,
                                                                           id_minta)
        else:
            print("Maaf, perintah ini hanya tersedia untuk user. Silakan login sebagai user (perintah : login).")
    elif command == "hborrow":
        if role == "admin":
            riwayat_gadget.riwayatPinjamGadget(gadget_borrow_history, user, gadget)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "hreturn":
        if role == "admin":
            riwayat_gadget.riwayatBalikGadget(gadget_return_history, user, gadget, gadget_borrow_history)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "hdemand":
        if role == "admin":
            riwayat_gadget.riwayatConsumable(consumable_history, user, consumable)
        else:
            print("Maaf, perintah ini hanya tersedia untuk admin program.")
    elif command == "save":
        if role:
            save_csv(consum_data, consum_hist_data, gadget_data, gadget_borrow_hist_data,
                     gadget_log_data, gadget_return_hist_data, user_data)
            
            consum_data = []
            consum_hist_data = []
            gadget_data = []
            gadget_borrow_hist_data = []
            gadget_log_data = []
            gadget_return_hist_data = []
            user_data = []
        else:
            print("Silakan login terlebih dahulu untuk menggunakan perintah ini (perintah : login).")
    elif command == "help":
        help_log.help(role)
    elif command == "exit":
        do_save = input("Apakah Anda ingin melakukan penyimpanan file?: (y/n) ").upper()

        if do_save not in ("Y", "N"):
            print("Masukan tidak valid. Harap ulangi!")
            continue
        elif do_save == "Y":
            save_csv(consum_data, consum_hist_data, gadget_data, gadget_borrow_hist_data,
                     gadget_log_data, gadget_return_hist_data, user_data)
        else:
            pass

        break
    else:
        print("Perintah tidak valid! Gunakan perintah 'help' untuk melihat daftar perintah yang tersedia.")
