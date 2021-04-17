# Library item_interaction
# Contains functions and procedures required to interact with items
# Contributor : 16520086

# Function add_item
# Adds a new item into the database

# Dictionary
# rarity_list : tuple
# item_id : str
# gad_name, gad_desc, gad_rarity : str
# gad_amount, gad_year : int
# con_name, con_desc, con_rarity : str
# con_amount : int
# new_consumable : list

# Algorithm
def add_item(gadget_database, consumable_database):
    rarity_list = ("S", "A", "B", "C")

    item_id = input("Input gadget ID: ")

    # Checks membership of item_id in every sublist of gadget_database and consumable_database
    if any(item_id in _ for _ in gadget_database) or any(item_id in _ for _ in consumable_database):
        print("Add item failed, item already existed!")
    elif item_id[0] not in ("G", "C"):  # Item ID is invalid
        print("Add item failed, item ID is invalid!")
    elif item_id[0] == "G":  # Item is a gadget
        gad_name = input("Input gadget name: ")
        gad_desc = input("Input gadget description: ")
        gad_amount = int(input("Input amount of gadget: "))
        if gad_amount <= 0:
            print("Add gadget failed, gadget amount is invalid!")
        else:
            gad_rarity = input("Input gadget rarity: ")
            if gad_rarity not in rarity_list:
                print("Add gadget failed, gadget rarity is invalid!")
            else:
                gad_year = int(input("Input gadget found year: "))
                if gad_year <= 0:
                    print("Add gadget failed, gadget year is invalid!")
                else:
                    new_gadget = [item_id, gad_name, gad_desc, gad_amount, gad_rarity, gad_year]
                    gadget_database.append(new_gadget)
    else:  # Item is a consumable
        con_name = input("Input consumable name: ")
        con_desc = input("Input consumable description: ")
        con_amount = int(input("Input amount of consumable: "))
        if con_amount <= 0:
            print("Add consumable failed, consumable amount is invalid!")
        else:
            con_rarity = input("Input consumable rarity: ")
            if con_rarity not in rarity_list:
                print("Add consumable failed, consumable rarity is invalid!")
            else:
                new_consumable = [item_id, con_name, con_desc, con_amount, con_rarity]
                consumable_database.append(new_consumable)


# Function delete_item
# Deletes an existing item from the database

# Dictionary
# item_id : str
# confirm : str
# item_index : int

# Algorithm
def delete_conf(database, item_index):
    confirm = input(f"Are you sure to delete {database[item_index][1]} (y/n)? ")
    if confirm == "y":
        del database[item_index]
        print("Item has been successfully removed!")
    else:
        pass  # Program does nothing if user selects "n"


def delete_item(gadget_database, consumable_database):
    item_id = input("Input gadget ID: ")

    # Checks membership of item_id in gadget_database
    if any(item_id in _ for _ in gadget_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _, _] in gadget_database].index(item_id)
        delete_conf(gadget_database, item_index)
    # Checks membership of item_id in consumable_database
    elif any(item_id in _ for _ in consumable_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _] in consumable_database].index(item_id)
        delete_conf(consumable_database, item_index)
    else:  # item_id isn't found
        print("Delete item failed. Item doesn't exist!")


# Function modify_item_amount
# Modifies item amount in the database

# Dictionary
# item_id : str
# amount : int
# item_index : int

# Algorithm
def amount_check(database, item_index):
    amount = int(input("Input amount to modify: "))

    # Modifies the gadget amount accordingly
    if database[item_index][3] + amount >= 0:
        database[item_index][3] += amount
        print(f"{amount} {database[item_index][1]} has been added. "
              f"Current amount: {database[item_index][3]}")
    else:
        print(f"Modify amount of {database[item_index][1]} failed due to insufficient item amount. "
              f"Current amount: {database[item_index][3]}")


def modify_item_amount(gadget_database, consumable_database):
    item_id = input("Input item ID: ")

    if any(item_id in _ for _ in gadget_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _, _] in gadget_database].index(item_id)
        amount_check(gadget_database, item_index)
    elif any(item_id in _ for _ in consumable_database):
        # Unpacks the nested list in order to be indexed
        item_index = [item_id for [item_id, _, _, _, _] in consumable_database].index(item_id)
        amount_check(consumable_database, item_index)
    else:
        print("Modify item amount failed. Item doesn't exist!")


# Use these for testing!
gadget = [["G5", "Car key", "Stolen for the lost boys.", 1, "A", 2010],
          ["G6", "Pocket knife", "Carved your name with it!", 1, "B", 2014]]
consum = [["C5", "Jumpsuit", "If you need anyone..", 1, "A"],
          ["C4", "Strawberry swing", "Wouldn't want to waste a thing..", 2, "S"]]

if __name__ == "__main__":
    modify_item_amount(gadget, consum)
    print(f"Gadget : {gadget}")
    print(f"Consum : {consum}")
