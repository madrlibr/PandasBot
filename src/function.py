def finfo(data): #this function can't work yet
    data = data.info()
    return data
            
def fdescribe(data):
    data = data.describe()
    return data
        
def fhead(data, n):
    data = data.head(n)
    return data
        
def fdropna(data):
    data = data.dropna()
    return data
        
def ftail(data, n):
    data = data.tail(n)
    return data

class makeice:
    def __init__(self, data):
        self.data = data
        self.length = len(data.columns)
        self.container = {}

    def breakice(self):
        for i in range(0, self.length):
            key = int(i)
            self.container[key] = self.data.iloc[:, i]


def select_column(data, n):
    obj = makeice(data)
    obj.breakice()
    try:
        return obj.container[n]
    except:
        pass

def meancolumn(data, integers):
    column = select_column(data, integers)
    try:
        mean = round((column).mean(), 2)
        return mean
    except:
        message = "Kesalahan, tidak dapat melakukan operasi, pastikan tipe data kolom adalah integer atau float"
        return message

def mediancolumn(data, integers):
    column = select_column(data, integers)
    try:
        median = round((column).median(), 2)
        return median
    except:
        message = "Kesalahan, tidak dapat melakukan operasi, pastikan tipe data kolom adalah integer atau float"
        return message

def sumcolumn(data, integers):
    column = select_column(data, integers)
    if column.dtype.kind in 'ifu':
        summ = column.sum()
        return summ
    else:
        message = "Kesalahan, tidak dapat melakukan operasi, pastikan tipe data kolom adalah integer atau float"
        return message
    
def check_dtype(data, n):
    column = select_column(data, n)
    dtype = (column.dtype)
    return dtype

def changer(type:str, input, n, data):
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
    #There's still a problem, and that is i can't yet change the dtype permanently, so i'm still working on it
    #and maybe i do overengineering, because when i think again, makeice class is not necessary and there's must be a simple way to pick a column

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