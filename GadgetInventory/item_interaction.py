# Library item_interaction
# Contains functions and procedures required to interact with items
# Contributor : 16520086
# Tester : 16520006

# Function add_item
# Adds a new item into the database

# Dictionary
# rarity_list : tuple
# item_id : str
# gad_name, gad_desc, gad_rarity : str
# gad_amount, gad_year : int
# new_gadget : list
# con_name, con_desc, con_rarity : str
# con_amount : int
# new_consumable : list

# Algorithm
def add_item(gadget_database, consumable_database):
    rarity_list = ("S", "A", "B", "C")

    item_id = input("Masukkan ID item: ")

    # Checks membership of item_id in every sublist of gadget_database and consumable_database
    if any(item_id in _ for _ in gadget_database) or any(item_id in _ for _ in consumable_database):
        print("Penambahan item gagal. Item sudah ada!")
    elif item_id[0] not in ("G", "C"):  # Item ID is invalid
        print("Penambahan item gagal. ID item invalid!")
    elif item_id[0] == "G":  # Item is a gadget
        gad_name = input("Masukkan nama gadget: ")
        gad_desc = input("Masukkan deskripsi gadget: ")
        gad_amount = int(input("Masukkan jumlah gadget: "))
        if gad_amount <= 0:
            print("Penambahan gadget gagal. Jumlah gadget invalid!")
        else:
            gad_rarity = input("Masukkan rarity gadget: ")
            if gad_rarity not in rarity_list:
                print("Penambahan gadget gagal. Rarity gadget invalid!")
            else:
                gad_year = int(input("Masukkan tahun penemuan gadget: "))
                if gad_year <= 0:
                    print("Penambahan gadget gagal. Tahun penemuan gadget invalid!")
                else:
                    new_gadget = [item_id, gad_name, gad_desc, gad_amount, gad_rarity, gad_year]
                    gadget_database.append(new_gadget)
    else:  # Item is a consumable
        con_name = input("Masukkan nama consumable: ")
        con_desc = input("Masukkan deskripsi consumable: ")
        con_amount = int(input("Masukkan jumlah consumable: "))
        if con_amount <= 0:
            print("Penambahan consumable gagal. Jumlah consumable invalid!")
        else:
            con_rarity = input("Masukkan rarity consumable: ")
            if con_rarity not in rarity_list:
                print("Penambahan consumable gagal. Rarity consumable invalid!")
            else:
                new_consumable = [item_id, con_name, con_desc, con_amount, con_rarity]
                consumable_database.append(new_consumable)

    print("Item telah berhasil ditambahkan ke database!")
    return gadget_database, consumable_database


# Function delete_item
# Deletes an existing item from the database

# Dictionary
# modified_gadget_database : list
# modified_consumable_database : list
# gadget_modified : int
# consum_modified : int
# item_id : str
# confirm : str
# item_index : int
# return_list : list
# tracker : int

# Algorithm
def delete_conf(database, item_index):
    confirm = input(f"Apakah Anda yakin ingin menghapus {database[item_index][1]} (y/n)? ")
    if confirm == "y":
        del database[item_index]
        print("Item telah berhasil dihapus dari database!")
        return database, 1
    else:
        return [], 0  # Program indicates nothing happened if user selects "n"


def delete_item(gadget_database, consumable_database):
    modified_gadget_database = []
    modified_consumable_database = []
    gadget_modified = 0
    consum_modified = 0

    item_id = input("Masukkan ID item: ")

    # Checks membership of item_id in gadget_database
    if any(item_id in _ for _ in gadget_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _, _] in gadget_database].index(item_id)
        return_list, tracker = delete_conf(gadget_database, item_index)
        modified_gadget_database += return_list
        gadget_modified += tracker
    # Checks membership of item_id in consumable_database
    elif any(item_id in _ for _ in consumable_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _] in consumable_database].index(item_id)
        return_list, tracker = delete_conf(consumable_database, item_index)
        modified_consumable_database += return_list
        consum_modified += tracker
    else:  # item_id isn't found
        print("Penghapusan item gagal. Item tidak ditemukan!")

    if gadget_modified:
        return modified_gadget_database, consumable_database
    elif consum_modified:
        return gadget_database, modified_consumable_database
    else:
        return gadget_database, consumable_database


# Function modify_item_amount
# Modifies item amount in the database

# Dictionary
# item_id : str
# amount : int
# item_index : int

# Algorithm
def amount_check(database, item_index):
    amount = int(input("Masukkan perubahan jumlah: "))

    # Modifies the gadget amount accordingly
    if database[item_index][3] + amount >= 0:
        database[item_index][3] += amount
        print(f"{amount} {database[item_index][1]} telah ditambahkan. "
              f"Jumlah sekarang: {database[item_index][3]}")
        return database, 1
    else:
        print(f"Perubahan jumlah {database[item_index][1]} gagal karena kurangnya jumlah item. "
              f"Jumlah sekarang: {database[item_index][3]}")
        return database, 0


def modify_item_amount(gadget_database, consumable_database):
    modified_gadget_database = []
    modified_consumable_database = []
    gadget_modified = 0
    consum_modified = 0

    item_id = input("Masukkan ID item: ")

    if any(item_id in _ for _ in gadget_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _, _] in gadget_database].index(item_id)
        return_list, tracker = amount_check(gadget_database, item_index)
        modified_gadget_database += return_list
        gadget_modified += tracker
    elif any(item_id in _ for _ in consumable_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _] in consumable_database].index(item_id)
        return_list, tracker = amount_check(consumable_database, item_index)
        modified_consumable_database += return_list
        consum_modified += tracker
    else:  # item_id isn't found
        print("Perubahan jumlah item gagal. Item tidak ditemukan!")

    if gadget_modified:
        return modified_gadget_database, consumable_database
    elif consum_modified:
        return gadget_database, modified_consumable_database
    else:
        return gadget_database, consumable_database


# Use these for testing!
# gadget = [["G5", "Car key", "Stolen for the lost boys.", 1, "A", 2010],
#           ["G6", "Pocket knife", "Carved your name with it!", 1, "B", 2014]]
# consum = [["C5", "Jumpsuit", "If you need anyone..", 1, "A"],
#           ["C4", "Strawberry swing", "Wouldn't want to waste a thing..", 2, "S"]]

# if __name__ == "__main__":
#     modify_item_amount(gadget, consum)
#     print(f"Gadget : {gadget}")
#     print(f"Consum : {consum}")
