def dinfo(x): #this function isn't working yet
    x = x.info()
    return x
            
def ddescribe(x):
    x = x.describe()
    return x
        
def dhead(x, n):
    x = x.head(n)
    return x
        
def ddropna(x):
    x = x.dropna()
    return x
        
def dtail(x, n):
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


def pcolumn(x, n):
    obj = makeice(x)
    obj.breakice()
    try:
        return obj.container[n]
    except:
        pass