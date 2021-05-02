# Library database_io
# Contains functions and procedures required to handle database input and output from file
# Contributor : 16520056, 16520086
# Tester : 16520006

# Dependency
import os


# Function load
# Loads databases from a folder specified

# Dictionary
# manual_split : function
# raw_to_data : function
# change_data_type : function
# csv_parse : function
# csv_files : list
# databases : list
# data_list : list
# i : integer

# Algorithm
def manual_split(string):
    splitted_string = []
    slicing_init = 0

    # implementing .split() everytime a semicolon is met
    for i in range(len(string)):
        if string[i] == ";":
            sliced = string[slicing_init:i]
            splitted_string.append(sliced)
            slicing_init = i + 1
    splitted_string.append(string[slicing_init:])

    return splitted_string


def raw_to_data(raw_lines):
    raw_line_list = manual_split(raw_lines)
    line_list = [line.strip() for line in raw_line_list]

    return line_list


def change_data_type(data_type, database):
    database_copy = database[:]

    try:
        if data_type == "gadget":
            for j in range(len(database_copy)):
                for i in range(6):
                    if i == 3 or i == 5:
                        database_copy[j][i] = int(database_copy[j][i])

        elif data_type == "consum":
            for j in range(len(database_copy)):
                for i in range(5):
                    if i == 3:
                        database_copy[j][i] = int(database_copy[j][i])
                        
        elif data_type == "gadget_borrow":
            for j in range(len(database_copy)):
                for i in range(5):
                    if i == 4:
                        database_copy[j][i] = int(database_copy[j][i])
                        
        elif data_type == "gadget_log":
            for j in range(len(database_copy)):
                for i in range(3):
                    if i == 2:
                        database_copy[j][i] = int(database_copy[j][i])
                        
        elif data_type == "consum_history":
            for j in range(len(database_copy)):
                for i in range(5):
                    if i == 4:
                        database_copy[j][i] = int(database_copy[j][i])
        else:  # data_type == "user" or data_type == "gadget_return" or data_type == "gadget_borrow"
            pass
    except ValueError:
        pass

    return database_copy


def csv_parse(directory, files):
    f = open(f"{directory}/{files}", "r")
    raw_lines = f.readlines()
    f.close()

    datas = []
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = raw_to_data(raw_header)
    datas.append(header)

    for line in lines:
        data_list = raw_to_data(line)
        datas.append(data_list)

    return datas


def load(folder_name):
    csv_files = []
    databases = []

    if folder_name:
        for roots, dirs, files in os.walk(str(folder_name)):
            # Files from os.walk is unordered and random every time. Sorting must be done to
            # ensure correct assignment by the main program.
            files.sort()
            csv_files += files

        for file in csv_files:
            data_list = csv_parse(folder_name, file)
            databases.append(data_list)

        return databases
    else:
        print("Load database failed. Folder name isn't specified!")


# Function save
# Saves databases to a folder specified

# Dictionary
# revert_data_type : function

# Algorithm
def revert_data_type(data_list):
    header = data_list.pop(0)
    csv = ";".join(header) + "\n"

    for item in data_list:
        csv_data = [str(data) for data in item]
        csv += ";".join(csv_data)
        csv += "\n"

    return csv


def save(folder_name, file_name, data):
    # Checks whether such folder exists, creates one if not
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    os.chdir(folder_name)
    # checks whether such file exists in the folder
    if not os.path.exists(file_name):  # file doesn't exist
        f = open(file_name, "x")  # creates the file and initialises it to be written
        f.write(data)
        f.close()
    else:  # file exists
        f = open(file_name, "w")  # prepares the file to be written
        f.write(data)
        f.close()

    os.chdir("..")
