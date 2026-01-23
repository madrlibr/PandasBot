import io

def finfo(data):
    buffer = io.StringIO()
    data.info(buf=buffer)
    return buffer.getvalue()
            
def fdescribe(data):
    data = data.describe()
    return data
        
def fhead(data, n):
    data = data.head(n)
    return data
        
def fdropna(data):
    data = data.dropna(inplace=True)
    return data
        
def ftail(data, n):
    data = data.tail(n)
    return data

def select_column(data, n):
    try:
        column = data.iloc[:, n]
        return column
    except:
        pass

def mean_column(data, n):
    column = select_column(data, n)
    try:
        mean = round((column).mean(), 2)
        return mean
    except:
        message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        return message

def median_column(data, n):
    column = select_column(data, n)
    try:
        median = round((column).median(), 2)
        return median
    except:
        message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        return message

def sum_column(data, n):
    column = select_column(data, n)
    try:
        if column.dtype.kind in 'ifu':
            summ = column.sum()
            return summ
        else:
            message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
            return message
    except:
        message = "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        return message
    
def check_dtype(data, n):
    try:
        column = select_column(data, n)
        dtype = (column.dtype)
        return dtype
    except:
        m = f"Kesalahan! tidak ada kolom dengan index ke-{n}"
        return m
    
def changer(type, input, n, data):
    input = input.split()
    column = data.iloc[:, n]
    getdtypef = (column.dtype)
    if type in input:   
        try:
            data.iloc[:, n] = data.iloc[:, n].astype(type)
            columnS = data.iloc[:, n] 
            getdtype = (columnS.dtype)
            m = f"Mengubah tipe data kolom index ke-{n}, dari {getdtypef} ke {getdtype} "
            return m
        except:
            m = "Terjadi kesalahan!"
            return m

def change_type(user_input, n, data):
    integers = "int"
    floats = "float"
    strings = "string"
    if integers in user_input:
        change = changer(integers, user_input, n, data)
        return change
    if floats in user_input:
        change = changer(floats, user_input, n, data)
        return change
    if strings in user_input:
        change = changer(strings, user_input, n, data)
        return change