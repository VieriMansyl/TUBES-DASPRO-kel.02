def arraydata_to_realvalue(file_name,array_data):
    arr_copy = array_data[:]
    if file_name == "data_tes":
        for i in range(6):
            if(i == 3 or i == 5):
                arr_copy[i] = int(arr_copy[i])
    elif file_name == "consume_tes":
        for i in range(5):
            if i == 3:
                arr_copy[i] = int(arr_copy[i])
    return arr_copy

def line_to_data(line):
    raw_array_of_data = line.split(";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def csv_to_data(file_name):
    if file_name == "data_tes":
        f = open("data_tes.csv","r")
    elif file_name == "consume_tes":
        f = open("consume_tes.csv","r")
    
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = line_to_data(raw_header)
    datas = []

    for line in lines:
        array_of_data = line_to_data(line)
        real_values = arraydata_to_realvalue(file_name , array_of_data)
        datas.append(real_values)
    
    return header, datas

nama_file = input('nama file\n>>>')
header, datas = csv_to_data(nama_file)