import numpy as np

def finfo(x): #this function isn't working yet
    x = x.info()
    return x
            
def fdescribe(x):
    x = x.describe()
    return x
        
def fhead(x, n):
    x = x.head(n)
    return x
        
def fdropna(x):
    x = x.dropna()
    return x
        
def ftail(x, n):
    x = x.tail(n)
    return x

class makeice:
    def __init__(self, data):
        self.data = data
        self.length = len(data.columns)
        self.container = {}

    def breakice(self):
        for i in range(0, self.length):
            key = int(i)
            self.container[key] = self.data.iloc[:, i]


def select_column(x, n):
    obj = makeice(x)
    obj.breakice()
    try:
        return obj.container[n]
    except:
        pass

def meancolumn(data, integers):
    try:
        column = select_column(data, integers)
        mean = round((column).mean(), 2)
        return mean
    except:
        message = "Kesalahan, tidak dapat melakukan operasi, pastikan tipe data kolom adalah integer atau float"
        return message

def mediancolumn(data, integers):
    try:
        column = select_column(data, integers)
        median = round((column).median(), 2)
        return median
    except:
        message = "Kesalahan, tidak dapat melakukan operasi, pastikan tipe data kolom adalah integer atau float"
        return message

def sumcolumn(data, integers):
    try:
        column = select_column(data, integers)
        summ = column.sum()
        return summ
    except:
        message = "Kesalahan, tidak dapat melakukan operasi, pastikan tipe data kolom adalah integer atau float"
        return message